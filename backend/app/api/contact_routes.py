"""
Contact API Routes
Defines HTTP endpoints for contact form operations
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import ContactFormSubmit, ContactFormResponse
from app.services import ContactService
from app.database import get_db
from app.core.dependencies import get_contact_service

router = APIRouter(prefix="/restaurants/{restaurant_id}/contact", tags=["Contact"])


@router.post("", response_model=ContactFormResponse, summary="Submit contact form", status_code=200)
async def submit_contact_form(
    restaurant_id: str,
    form_data: ContactFormSubmit,
    db: Session = Depends(get_db)
):
    """
    Submit a contact form message
    
    - **restaurant_id**: Unique restaurant identifier
    - **name**: Sender's full name
    - **email**: Sender's email address
    - **subject**: Optional subject line
    - **message**: Message content
    """
    try:
        service = get_contact_service(db)
        response = service.submit_contact_form(restaurant_id, form_data)
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send message")
