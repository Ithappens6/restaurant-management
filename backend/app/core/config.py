"""
Core Configuration Module
Handles application settings and environment variables
Following Single Responsibility Principle
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings and configuration"""
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    
    # CORS Configuration
    cors_origins: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "https://a8181d952605.ngrok-free.app"
    ]
    
    # Restaurant Information
    restaurant_name: str = "Kurdie's Curry"
    restaurant_address: str = "1337 N Spice Rd, Prescott Valley, AZ 86314"
    restaurant_phone: str = "(928) 555-1337"
    
    # Business Hours (24-hour format)
    # Format: {day: (open_hour, close_hour)} or None for closed
    business_hours: dict = {
        0: None,  # Sunday - CLOSED
        1: (11, 21),  # Monday: 11am-9pm
        2: (11, 21),  # Tuesday: 11am-9pm
        3: (11, 21),  # Wednesday: 11am-9pm
        4: (11, 21),  # Thursday: 11am-9pm
        5: (11, 22),  # Friday: 11am-10pm
        6: (11, 22),  # Saturday: 11am-10pm
    }
    
    # OpenAI Configuration
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Singleton instance
settings = Settings()

