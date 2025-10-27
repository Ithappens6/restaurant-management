"""
Reservation API Routes
Defines HTTP endpoints for reservation operations
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import ReservationCreate, ReservationConfirmation
from app.services import ReservationService
from app.database import get_db
from app.core.dependencies import get_reservation_service

router = APIRouter(prefix="/restaurants/{restaurant_id}/reservations", tags=["Reservations"])


@router.post("", response_model=ReservationConfirmation, summary="Create a reservation", status_code=201)
async def create_reservation(
    restaurant_id: str,
    reservation_data: ReservationCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new restaurant reservation
    
    - **restaurant_id**: Unique restaurant identifier
    - **name**: Customer's full name
    - **email**: Customer's email address
    - **phone**: Customer's phone number
    - **date**: Reservation date (YYYY-MM-DD format)
    - **time**: Reservation time (HH:MM format, 24-hour)
    - **party_size**: Number of guests (1-20)
    - **special_requests**: Optional special requests or dietary notes
    """
    try:
        service = get_reservation_service(db)
        confirmation = service.create_reservation(restaurant_id, reservation_data)
        return confirmation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create reservation")


@router.get("/{reservation_id}", summary="Get reservation details")
async def get_reservation(
    restaurant_id: str,
    reservation_id: str,
    db: Session = Depends(get_db)
):
    """
    Get details of a specific reservation
    
    - **restaurant_id**: Unique restaurant identifier
    - **reservation_id**: The unique reservation ID
    """
    service = get_reservation_service(db)
    reservation = service.get_reservation(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if reservation.restaurant_id != restaurant_id:
        raise HTTPException(status_code=404, detail="Reservation not found for this restaurant")
    return reservation


@router.delete("/{reservation_id}", summary="Cancel a reservation")
async def cancel_reservation(
    restaurant_id: str,
    reservation_id: str,
    db: Session = Depends(get_db)
):
    """
    Cancel an existing reservation
    
    - **restaurant_id**: Unique restaurant identifier
    - **reservation_id**: The unique reservation ID
    """
    service = get_reservation_service(db)
    
    # Verify reservation belongs to this restaurant
    reservation = service.get_reservation(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    if reservation.restaurant_id != restaurant_id:
        raise HTTPException(status_code=404, detail="Reservation not found for this restaurant")
    
    success = service.cancel_reservation(reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return {"success": True, "message": "Reservation cancelled successfully"}
