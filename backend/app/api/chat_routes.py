"""
Chat API Routes
Defines HTTP endpoints for chat operations
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.chat_schemas import ChatMessageRequest, ChatResponse, ChatHistoryResponse
from app.services.chat_service import ChatService
from app.services.reservation_service import ReservationService
from app.database import get_db
from app.core.dependencies import get_restaurant_service, get_reservation_service
from app.repositories.sqlalchemy_chat_repository import SQLAlchemyChatRepository

router = APIRouter(prefix="/restaurants/{restaurant_id}/chat", tags=["Chat"])


def get_chat_service(db: Session = Depends(get_db)) -> ChatService:
    """
    Get chat service instance with database session and reservation service
    """
    from app.core.dependencies import get_restaurant_repository
    chat_repository = SQLAlchemyChatRepository(db)
    restaurant_repository = get_restaurant_repository()
    from app.services.restaurant_service import RestaurantService
    restaurant_service = RestaurantService(restaurant_repository)
    reservation_service = get_reservation_service(db)
    return ChatService(chat_repository, restaurant_service, reservation_service, db=db)


@router.post("", response_model=ChatResponse, summary="Send a chat message", status_code=200)
async def send_message(
    restaurant_id: str,
    request: ChatMessageRequest,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Send a message to the restaurant's AI assistant
    
    - **restaurant_id**: Unique restaurant identifier
    - **session_id**: Unique session identifier for conversation continuity
    - **message**: User's message to the AI assistant
    
    The AI will respond based on the restaurant's information and chat history.
    """
    try:
        # Validate restaurant_id matches request
        if request.restaurant_id != restaurant_id:
            raise HTTPException(
                status_code=400, 
                detail="Restaurant ID in URL must match restaurant_id in request body"
            )
        
        response = chat_service.process_message(request)
        return response
        
    except ValueError as e:
        print(f"❌ ValueError in chat route: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"❌ Exception in chat route: {str(e)}")
        import traceback
        print(f"❌ Traceback:\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Failed to process chat message: {str(e)}")


@router.get("/history/{session_id}", response_model=ChatHistoryResponse, summary="Get chat history")
async def get_chat_history(
    restaurant_id: str,
    session_id: str,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Get chat history for a specific session
    
    - **restaurant_id**: Unique restaurant identifier
    - **session_id**: Unique session identifier
    
    Returns all messages in the conversation ordered by creation time.
    """
    try:
        history = chat_service.get_chat_history(session_id, restaurant_id)
        return history
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve chat history")


@router.post("/session", summary="Generate new session ID")
async def generate_session(
    restaurant_id: str,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Generate a new session ID for starting a chat conversation
    
    - **restaurant_id**: Unique restaurant identifier
    
    Returns a unique session ID that can be used for subsequent chat messages.
    """
    try:
        session_id = chat_service.generate_session_id(restaurant_id)
        return {
            "success": True,
            "session_id": session_id,
            "message": "New session created successfully"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate session ID")


@router.post("/rebuild-prompt", summary="Rebuild system prompt")
async def rebuild_prompt(
    restaurant_id: str,
    chat_service: ChatService = Depends(get_chat_service)
):
    """
    Force rebuild of the AI system prompt for this restaurant
    
    - **restaurant_id**: Unique restaurant identifier
    
    Call this endpoint when:
    - Restaurant information is updated
    - Menu items are changed
    - Business hours are modified
    - You want to clear the cache
    
    Returns statistics about the rebuilt prompt including token count and size.
    """
    try:
        result = chat_service.rebuild_system_prompt(restaurant_id)
        return result
        
    except Exception as e:
        print(f"❌ Error rebuilding prompt: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to rebuild prompt: {str(e)}")
