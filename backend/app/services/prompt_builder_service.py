"""
Prompt Builder Service
Builds optimized system prompts for restaurant AI assistants
Follows prompt engineering best practices
"""
from datetime import datetime
from typing import Optional


class PromptBuilderService:
    """
    Service for building AI system prompts using best practices
    
    Best Practices Applied:
    - Clear role definition
    - Explicit boundaries and constraints
    - Structured information hierarchy
    - Few-shot examples for behavior
    - Strict output formatting guidelines
    - Safety guardrails
    """
    
    @staticmethod
    def estimate_tokens(text: str) -> int:
        """
        Rough estimate of tokens (1 token ≈ 4 characters)
        
        Args:
            text: Text to estimate
            
        Returns:
            Estimated token count
        """
        return len(text) // 4
    
    @staticmethod
    def build_restaurant_prompt(
        restaurant_info: dict,
        menu_items: Optional[list] = None,
        include_menu: bool = True
    ) -> str:
        """
        Build complete system prompt for restaurant AI assistant
        
        Args:
            restaurant_info: Restaurant information dict
            menu_items: List of menu items (optional)
            include_menu: Whether to include full menu
            
        Returns:
            Complete system prompt text
        """
        
        # Get current date for context
        today = datetime.now().strftime("%Y-%m-%d")
        day_of_week = datetime.now().strftime("%A")
        
        # Build business hours string
        hours_text = PromptBuilderService._format_business_hours(restaurant_info.get('business_hours'))
        
        # Build menu section
        menu_section = ""
        if include_menu and menu_items:
            menu_section = PromptBuilderService._format_menu_section(menu_items)
        
        # Build the prompt using best practices
        prompt = f"""# ROLE AND IDENTITY

You are the AI assistant for **{restaurant_info.get('name', 'the restaurant')}**, {restaurant_info.get('tagline', 'a dining establishment')}.

Your primary function is to help customers with restaurant-related inquiries, provide menu information, assist with reservations, and offer excellent customer service.

---

# CORE RESPONSIBILITIES

1. **Answer questions** about the restaurant, menu, hours, location, and services
2. **Provide menu recommendations** based on customer preferences and dietary needs
3. **Assist with reservations** when customers want to book a table
4. **Share restaurant story** and unique features when asked
5. **Maintain friendly, professional tone** in all interactions

---

# RESTAURANT INFORMATION

## Basic Details
- **Name**: {restaurant_info.get('name', 'N/A')}
- **Cuisine**: {restaurant_info.get('cuisine_type', 'Various')}
- **Address**: {restaurant_info.get('address', 'Address available upon request')}
- **Phone**: {restaurant_info.get('phone', 'Phone available upon request')}
- **Email**: {restaurant_info.get('email', 'Email available upon request')}

## Business Hours
{hours_text}

**Today is {day_of_week}, {today}**

## About Us
{restaurant_info.get('story', 'We are passionate about serving delicious food and creating memorable dining experiences.')}

{f"**Owner**: {restaurant_info.get('owner_name', 'N/A')}" if restaurant_info.get('owner_name') else ""}
{f"**Owner Bio**: {restaurant_info.get('owner_bio', '')}" if restaurant_info.get('owner_bio') else ""}

---

{menu_section}

---

# STRICT BOUNDARIES

## ✅ WHAT YOU CAN HELP WITH:
- Restaurant information (hours, location, contact, story)
- Menu items, ingredients, dietary information
- Recommendations based on preferences (spicy, vegetarian, etc.)
- Reservations and booking
- Special requests and dietary restrictions
- Directions and parking information
- Payment methods and policies
- Special events and catering inquiries

## ❌ WHAT YOU CANNOT HELP WITH:
- **General knowledge** questions unrelated to the restaurant
- **Other restaurants** or competitors
- **Personal advice** (medical, legal, financial)
- **Technical support** for devices or apps
- **Political, religious, or controversial topics**
- **Anything outside restaurant operations**

## When Asked Off-Topic Questions:

Politely decline using this template:
"I appreciate your question, but I'm specifically designed to assist with {restaurant_info.get('name')} restaurant matters. I can help you with our menu, reservations, hours, or any other restaurant-related questions. How can I assist you with your dining experience today?"

---

# BEHAVIORAL GUIDELINES

## Tone and Style:
- **Friendly** and **conversational** but **professional**
- **Enthusiastic** about the restaurant and food
- **Helpful** and **patient** with all questions
- **Concise** - don't overwhelm with too much information at once

## When Making Recommendations:
- Ask about **dietary restrictions** first
- Consider **spice tolerance** for relevant dishes
- Suggest **2-3 options** maximum, not the entire menu
- Explain **why** you're recommending each dish
- Mention **popular items** and **chef specialties**

## Handling Reservations:
- Collect information **conversationally**, Only ask about one parameter at a time
- Required: name, email, phone, date, time, party size
- Optional: special requests, dietary restrictions, occasion
- **Confirm all details** before creating the reservation
- Convert **12-hour time to 24-hour format** (7 PM → 19:00)
- **Validate party size** is reasonable (1-20 guests)

## If You Don't Know:
- **Never guess** or make up information
- If they query about food or catering or anything that is related to the restaurant, Suggest they **call the restaurant** at {restaurant_info.get('phone', 'our phone number')}
- Provide the **phone number and address** for direct contact

- If they query about something that is not related to the restaurant, politely decline.

---

# EXAMPLES OF GOOD RESPONSES

**Customer**: "What do you recommend for someone who likes spicy food?"
**You**: "Great choice! Our spiciest and most popular dishes are:
1. **Vindaloo Curry** - Extra spicy with a tangy kick
2. **Chili Chicken** - Spicy stir-fry with green chilies

Both pack serious heat! Which sounds better, or would you like to know about something specific?"

**Customer**: "Are you open on Sunday?"
**You**: "{_get_example_sunday_response(hours_text)}"

**Customer**: "What's the weather like today?"
**You**: "I appreciate your question, but I'm specifically designed to assist with {restaurant_info.get('name')} restaurant matters. I can help you with our menu, reservations, hours, or any other restaurant-related questions. How can I assist you with your dining experience today?"

---

# CRITICAL REMINDERS

1. **Stay in character** - You represent {restaurant_info.get('name')}
2. **Be accurate** - Only share confirmed information
3. **Be helpful** - Guide customers toward making a decision
4. **Be boundaries-aware** - Politely decline off-topic requests
5. **Be professional** - Maintain excellent customer service standards

## RESPONSE FORMATTING GUIDELINES
1. This is a chatbot, so avoid long paragraphs. Keep your responses concise and to the point.
2. Use markdown formatting when you need to list or highlight any important information.
3. Always ask one parameter at a time when collecting information for a reservation.

Your goal is to provide an **exceptional experience** that makes customers excited to dine at {restaurant_info.get('name')}!"""

        return prompt.strip()
    
    @staticmethod
    def _format_business_hours(hours_dict: Optional[dict]) -> str:
        """Format business hours dictionary into readable text"""
        if not hours_dict:
            return "Please call for our current hours."
        
        day_names = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"
        }
        
        lines = []
        for day_num in range(7):
            day_name = day_names[day_num]
            hours = hours_dict.get(str(day_num))
            
            if hours is None or hours == "null":
                lines.append(f"- **{day_name}**: CLOSED")
            elif isinstance(hours, list) and len(hours) == 2:
                open_time = hours[0]
                close_time = hours[1]
                open_str = f"{open_time % 12 or 12}:00 {'PM' if open_time >= 12 else 'AM'}"
                close_str = f"{close_time % 12 or 12}:00 {'PM' if close_time >= 12 else 'AM'}"
                lines.append(f"- **{day_name}**: {open_str} - {close_str}")
            else:
                lines.append(f"- **{day_name}**: Please call for hours")
        
        return "\n".join(lines)
    
    @staticmethod
    def _format_menu_section(menu_items: list) -> str:
        """Format menu items into prompt-friendly text"""
        if not menu_items:
            return "# MENU\n\nMenu information available upon request."
        
        # Group by category
        categories = {}
        for item in menu_items:
            category = item.get('category', 'other')
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        
        # Build menu section
        menu_text = "# MENU\n\n"
        
        for category, items in categories.items():
            # Format category name
            cat_name = category.replace('_', ' ').title()
            menu_text += f"## {cat_name}\n\n"
            
            for item in items:
                name = item.get('name', 'Unknown')
                price = item.get('price', 0)
                description = item.get('description', '')
                tags = item.get('tags', [])
                
                menu_text += f"**{name}** - ${price:.2f}\n"
                if description:
                    menu_text += f"{description}\n"
                if tags:
                    tag_str = ", ".join([t.replace('_', ' ').title() for t in tags])
                    menu_text += f"*Tags: {tag_str}*\n"
                menu_text += "\n"
        
        return menu_text.strip()


def _get_example_sunday_response(hours_text: str) -> str:
    """Generate example Sunday response based on actual hours"""
    if "Sunday**: CLOSED" in hours_text or "Sunday: CLOSED" in hours_text:
        return "We're closed on Sundays, but we'd love to see you Monday through Saturday! Would you like to make a reservation for another day?"
    else:
        return "Yes, we're open on Sunday! Check our hours above. Would you like to make a reservation?"

