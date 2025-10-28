"""
Chat Service
Business logic for chat operations with OpenAI integration
"""
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from app.repositories.sqlalchemy_chat_repository import SQLAlchemyChatRepository
from app.repositories.prompt_cache_repository import PromptCacheRepository
from app.schemas.chat_schemas import ChatMessageRequest, ChatResponse, ChatHistoryResponse, ChatMessage
from app.schemas.reservation_schemas import ReservationCreate
from app.services.restaurant_service import RestaurantService
from app.services.reservation_service import ReservationService
from app.services.prompt_builder_service import PromptBuilderService
from openai import OpenAI
import os
import uuid
import json
from datetime import datetime


class ChatService:
    """
    Service for handling chat operations with OpenAI integration
    Supports function calling for reservations
    """
    
    def __init__(self, chat_repository: SQLAlchemyChatRepository, restaurant_service: RestaurantService, 
                 reservation_service: Optional[ReservationService] = None, db: Optional[Session] = None):
        self.chat_repository = chat_repository
        self.restaurant_service = restaurant_service
        self.reservation_service = reservation_service
        self.db = db
        self.prompt_cache_repo = PromptCacheRepository(db) if db else None
        self.prompt_builder = PromptBuilderService()
        
        # Initialize OpenAI client
        from app.core.config import settings
        api_key = settings.openai_api_key or os.getenv("OPENAI_API_KEY")
        
        if not api_key or api_key == "":
            raise ValueError("OPENAI_API_KEY is not configured in settings or environment")
        
        self.openai_client = OpenAI(api_key=api_key)
    
    def _get_reservation_tool_definition(self) -> Dict[str, Any]:
        """
        Define the reservation tool for OpenAI function calling
        """
        return {
            "type": "function",
            "function": {
                "name": "create_reservation",
                "description": "Create a restaurant reservation for the customer. Use this when the customer wants to make a reservation or book a table. Collect all required information before calling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Customer's full name"
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer's email address"
                        },
                        "phone": {
                            "type": "string",
                            "description": "Customer's phone number"
                        },
                        "date": {
                            "type": "string",
                            "description": "Reservation date in YYYY-MM-DD format (e.g., 2024-12-25)"
                        },
                        "time": {
                            "type": "string",
                            "description": "Reservation time in HH:MM format, 24-hour (e.g., 19:00 for 7 PM)"
                        },
                        "party_size": {
                            "type": "integer",
                            "description": "Number of guests (1-20)",
                            "minimum": 1,
                            "maximum": 20
                        },
                        "special_requests": {
                            "type": "string",
                            "description": "Optional special requests or dietary restrictions"
                        }
                    },
                    "required": ["name", "email", "phone", "date", "time", "party_size"]
                }
            }
        }
    
    def _handle_reservation_tool_call(self, tool_call_args: Dict[str, Any], restaurant_id: str) -> str:
        """
        Handle the reservation tool call by creating actual reservation
        """
        try:
            # Create reservation using the service
            if not self.reservation_service:
                return "I apologize, but I'm unable to create reservations at this time. Please call the restaurant directly."
            
            reservation_data = ReservationCreate(
                restaurant_id=restaurant_id,
                name=tool_call_args["name"],
                email=tool_call_args["email"],
                phone=tool_call_args["phone"],
                date=tool_call_args["date"],
                time=tool_call_args["time"],
                party_size=tool_call_args["party_size"],
                special_requests=tool_call_args.get("special_requests")
            )
            
            confirmation = self.reservation_service.create_reservation(restaurant_id, reservation_data)
            
            return json.dumps({
                "success": True,
                "reservation_id": confirmation.reservation_id,
                "message": "Reservation successfully created"
            })
            
        except Exception as e:
            return json.dumps({
                "success": False,
                "error": str(e),
                "message": "Failed to create reservation"
            })
    
    def process_message(self, request: ChatMessageRequest) -> ChatResponse:
        """
        Process a chat message and return AI response
        """
        session_id = request.session_id
        restaurant_id = request.restaurant_id
        user_message = request.message
        
        print(f"\n{'='*60}")
        print(f"📨 NEW CHAT REQUEST")
        print(f"{'='*60}")
        print(f"🆔 Session ID: {session_id}")
        print(f"🏪 Restaurant ID: {restaurant_id}")
        print(f"💬 User message: {user_message}")
        print(f"{'='*60}\n")
        
        # Get or create session
        session = self.chat_repository.get_session(session_id)
        if not session:
            print(f"🆕 Creating new session: {session_id}")
            session = self.chat_repository.create_session(session_id, restaurant_id)
        else:
            print(f"♻️  Using existing session: {session_id}")
        
        # Update session activity
        self.chat_repository.update_session_activity(session_id)
        
        # Store user message
        user_msg = self.chat_repository.create_message(
            session_id=session_id,
            restaurant_id=restaurant_id,
            role="user",
            content=user_message
        )
        
        # Get chat history for context (empty if none found)
        try:
            chat_history = self.chat_repository.get_session_messages(session_id, limit=20)
        except:
            chat_history = []
        
        # Get restaurant context (from cache or build fresh)
        try:
            restaurant_context = self._get_or_build_system_prompt(restaurant_id)
        except Exception as e:
            print(f"⚠️  Error getting system prompt: {e}")
            restaurant_context = "You are a helpful assistant for a restaurant."
        
        # Build conversation context for OpenAI
        messages = self._build_openai_messages(restaurant_context, chat_history)
        
        try:
            # Call OpenAI API with tools/functions
            tools = [self._get_reservation_tool_definition()] if self.reservation_service else []
            
            print(f"🤖 Calling OpenAI API for session: {session_id}")
            print(f"📝 Messages count: {len(messages)}")
            print(f"🔧 Tools enabled: {bool(tools)}")
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4.1",
                messages=messages,
                tools=tools if tools else None,
                tool_choice="auto" if tools else None,
                max_tokens=1000,
                temperature=0.7,
                stream=False
            )
            
            print(f"✅ OpenAI Response received")
            print(f"📊 Response ID: {response.id}")
            print(f"📊 Model used: {response.model}")
            print(f"📊 Finish reason: {response.choices[0].finish_reason}")
            
            response_message = response.choices[0].message
            
            print(f"💬 Response message content: {response_message.content}")
            print(f"🔧 Has tool calls: {bool(response_message.tool_calls)}")
            
            # Check if the model wants to call a function
            if response_message.tool_calls:
                # Handle tool calls (reservations)
                tool_call = response_message.tool_calls[0]
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                if function_name == "create_reservation":
                    print(f"🎯 Tool call detected: {function_name}")
                    print(f"📋 Function args: {function_args}")
                    
                    # Execute the reservation
                    function_response = self._handle_reservation_tool_call(function_args, restaurant_id)
                    print(f"📤 Function response: {function_response}")
                    
                    # Send the function response back to OpenAI to generate a natural response
                    messages.append({
                        "role": "assistant",
                        "content": None,
                        "tool_calls": [
                            {
                                "id": tool_call.id,
                                "type": "function",
                                "function": {
                                    "name": function_name,
                                    "arguments": tool_call.function.arguments
                                }
                            }
                        ]
                    })
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": function_response
                    })
                    
                    # Get the final response from OpenAI
                    print(f"🔄 Calling OpenAI again with function results...")
                    second_response = self.openai_client.chat.completions.create(
                        model="gpt-4.1",
                        messages=messages,
                        max_tokens=1000,
                        temperature=0.7
                    )
                    
                    assistant_message = second_response.choices[0].message.content
                    print(f"💬 Second response content: {assistant_message}")
                else:
                    assistant_message = "I'm not sure how to help with that."
            else:
                # No function call, use the regular response
                assistant_message = response_message.content
                print(f"✅ Regular response (no tool calls)")
            
            # Ensure we have a message
            if not assistant_message:
                print(f"⚠️  WARNING: Empty assistant message!")
                print(f"⚠️  Response object: {response}")
                print(f"⚠️  Response message: {response_message}")
                assistant_message = "I apologize, but I couldn't generate a response. Please try again."
            
            print(f"💾 Storing assistant message: {assistant_message[:100]}...")
            
            # Store assistant response
            assistant_msg = self.chat_repository.create_message(
                session_id=session_id,
                restaurant_id=restaurant_id,
                role="assistant",
                content=assistant_message
            )
            
            print(f"✅ Message stored with ID: {assistant_msg.id}")
            
            return ChatResponse(
                success=True,
                message="Message processed successfully",
                session_id=session_id,
                assistant_message=assistant_message,
                message_id=assistant_msg.id
            )
            
        except Exception as e:
            # Handle OpenAI API errors
            print(f"❌ ERROR in process_message: {str(e)}")
            print(f"❌ Error type: {type(e).__name__}")
            import traceback
            print(f"❌ Traceback:\n{traceback.format_exc()}")
            
            error_message = f"I apologize, but I'm having trouble processing your request right now. Please try again later."
            
            # Store error response
            error_msg = self.chat_repository.create_message(
                session_id=session_id,
                restaurant_id=restaurant_id,
                role="assistant",
                content=error_message
            )
            
            return ChatResponse(
                success=False,
                message=f"Error processing message: {str(e)}",
                session_id=session_id,
                assistant_message=error_message,
                message_id=error_msg.id
            )
    
    def get_chat_history(self, session_id: str, restaurant_id: str) -> ChatHistoryResponse:
        """
        Get chat history for a session
        """
        # Verify session exists and belongs to restaurant
        session = self.chat_repository.get_session(session_id)
        if not session or session.restaurant_id != restaurant_id:
            raise ValueError("Session not found or doesn't belong to this restaurant")
        
        messages = self.chat_repository.get_session_messages(session_id)
        total_messages = self.chat_repository.get_session_messages_count(session_id)
        
        return ChatHistoryResponse(
            session_id=session_id,
            restaurant_id=restaurant_id,
            messages=messages,
            total_messages=total_messages
        )
    
    def _get_or_build_system_prompt(self, restaurant_id: str) -> str:
        """
        Get system prompt from cache or build fresh
        
        Args:
            restaurant_id: Restaurant identifier
            
        Returns:
            System prompt text
        """
        # Try to get from cache first
        if self.prompt_cache_repo:
            cached_prompt = self.prompt_cache_repo.get_prompt(restaurant_id)
            if cached_prompt:
                print(f"✅ Using cached system prompt for {restaurant_id}")
                return cached_prompt
        
        # Cache miss - build fresh prompt
        print(f"🔨 Building fresh system prompt for {restaurant_id}")
        return self._build_fresh_system_prompt(restaurant_id, cache_it=False)
    
    def _build_fresh_system_prompt(self, restaurant_id: str, cache_it: bool = True) -> str:
        """
        Build a fresh system prompt using PromptBuilderService
        
        Args:
            restaurant_id: Restaurant identifier
            cache_it: Whether to cache the result
            
        Returns:
            Fresh system prompt
        """
        try:
            print(f"🔨 Building system prompt for restaurant: {restaurant_id}")
            
            # Get restaurant info
            restaurant_info = self.restaurant_service.get_restaurant(restaurant_id)
            if not restaurant_info:
                print(f"⚠️  Restaurant not found: {restaurant_id}")
                return "You are a helpful assistant for a restaurant."
            
            print(f"✅ Restaurant found: {restaurant_info.name if hasattr(restaurant_info, 'name') else 'Unknown'}")
            
            # Convert restaurant model to dict with safe attribute access
            restaurant_dict = {
                'name': getattr(restaurant_info, 'name', 'Restaurant'),
                'tagline': getattr(restaurant_info, 'tagline', ''),
                'address': getattr(restaurant_info, 'address', ''),
                'phone': getattr(restaurant_info, 'phone', ''),
                'email': getattr(restaurant_info, 'email', None),
                'cuisine_type': getattr(restaurant_info, 'cuisine_type', 'Various'),
                'story': getattr(restaurant_info, 'story', ''),
                'owner_name': getattr(restaurant_info, 'owner_name', None),
                'owner_bio': getattr(restaurant_info, 'owner_bio', None),
                'business_hours': getattr(restaurant_info, 'business_hours', {
                    "0": None,  # Sunday: Closed
                    "1": [11, 21],  # Monday: 11 AM - 9 PM
                    "2": [11, 21],  # Tuesday
                    "3": [11, 21],  # Wednesday
                    "4": [11, 21],  # Thursday
                    "5": [11, 21],  # Friday
                    "6": [11, 21]   # Saturday
                })
            }
            
            print(f"✅ Restaurant dict created with keys: {list(restaurant_dict.keys())}")
            
            # Get menu items if available
            menu_items = []
            try:
                from app.services.menu_service import MenuService
                from app.repositories import InMemoryRestaurantRepository
                from app.data import create_sample_restaurants
                
                # Get menu (simplified for now)
                # You can integrate menu service here if needed
                print(f"📋 Menu items: {len(menu_items)}")
            except Exception as menu_error:
                print(f"⚠️  Could not load menu: {menu_error}")
                menu_items = []
            
            # Build prompt using PromptBuilderService
            print(f"🏗️  Building prompt with PromptBuilderService...")
            prompt = self.prompt_builder.build_restaurant_prompt(
                restaurant_info=restaurant_dict,
                menu_items=menu_items,
                include_menu=True
            )
            print(f"✅ Prompt built successfully, length: {len(prompt)} characters")
            
            # Add reservation capability note if available
            if self.reservation_service:
                prompt += "\n\n" + """
---

# RESERVATION TOOL AVAILABLE

You have access to a `create_reservation` tool. When a customer wants to book a table:
- Collect ALL required information conversationally: name, email, phone, date (YYYY-MM-DD), time (HH:MM 24-hour), party size
- Ask about special requests or dietary restrictions
- Confirm all details with the customer before making the reservation
- Then use the tool to create the reservation
- Provide the confirmation details to the customer after the reservation is made

Remember: Convert 12-hour time to 24-hour format (e.g., 7 PM = 19:00)
"""
                print(f"✅ Added reservation tool instructions")
            
            # Cache it if requested
            if cache_it and self.prompt_cache_repo:
                estimated_tokens = self.prompt_builder.estimate_tokens(prompt)
                self.prompt_cache_repo.set_prompt(
                    restaurant_id=restaurant_id,
                    prompt_text=prompt,
                    includes_menu=bool(menu_items),
                    includes_hours=True,
                    includes_about=True,
                    estimated_tokens=estimated_tokens
                )
                print(f"💾 Cached system prompt for {restaurant_id} ({estimated_tokens} tokens)")
            
            print(f"✅ System prompt ready, returning {len(prompt)} characters")
            return prompt
        
        except Exception as e:
            print(f"❌ ERROR building system prompt: {str(e)}")
            import traceback
            print(f"❌ Traceback:\n{traceback.format_exc()}")
            # Return a basic prompt as fallback
            return "You are a helpful assistant for a restaurant. Assist customers with their questions about the menu, hours, and reservations."
    
    def rebuild_system_prompt(self, restaurant_id: str) -> dict:
        """
        Force rebuild of system prompt (call when restaurant data changes)
        
        Args:
            restaurant_id: Restaurant identifier
            
        Returns:
            Dict with prompt stats
        """
        prompt = self._build_fresh_system_prompt(restaurant_id, cache_it=True)
        
        # Get cache stats
        if self.prompt_cache_repo:
            stats = self.prompt_cache_repo.get_cache_stats(restaurant_id)
        else:
            stats = {
                "size_bytes": len(prompt),
                "estimated_tokens": self.prompt_builder.estimate_tokens(prompt)
            }
        
        return {
            "success": True,
            "restaurant_id": restaurant_id,
            "prompt_length": len(prompt),
            "stats": stats
        }
    
    def _build_openai_messages(self, restaurant_context: str, chat_history: List[ChatMessage]) -> List[dict]:
        """
        Build messages array for OpenAI API
        """
        messages = [
            {
                "role": "system",
                "content": restaurant_context
            }
        ]
        
        # Add chat history (last 10 messages to avoid token limits)
        recent_history = chat_history[-10:] if len(chat_history) > 10 else chat_history
        
        for msg in recent_history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        return messages
    
    def generate_session_id(self, restaurant_id: str) -> str:
        """
        Generate a unique session ID
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        random_id = str(uuid.uuid4())[:8]
        return f"{restaurant_id}_{timestamp}_{random_id}"
