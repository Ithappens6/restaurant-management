"""
SQLAlchemy Reservation Repository
Database implementation of reservation storage
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import Reservation
from app.database.models import ReservationModel
import uuid


class SQLAlchemyReservationRepository:
    """
    SQLAlchemy implementation of reservation repository
    Stores reservations in database with full persistence
    """
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Reservation]:
        """Get all reservations from database"""
        db_reservations = self.db.query(ReservationModel).all()
        
        return [
            self._to_domain(db_res) 
            for db_res in db_reservations
        ]
    
    def get_by_id(self, reservation_id: str) -> Optional[Reservation]:
        """Get reservation by ID from database"""
        db_reservation = self.db.query(ReservationModel).filter(
            ReservationModel.id == reservation_id
        ).first()
        
        if not db_reservation:
            return None
        
        return self._to_domain(db_reservation)
    
    def create(self, reservation: Reservation) -> Reservation:
        """Create a new reservation in database"""
        # Generate ID if not provided
        if not reservation.id:
            reservation.id = str(uuid.uuid4())[:8]
        
        # Convert domain entity to database model
        db_reservation = ReservationModel(
            id=reservation.id,
            restaurant_id=reservation.restaurant_id,
            name=reservation.name,
            email=reservation.email,
            phone=reservation.phone,
            date=reservation.date,
            time=reservation.time,
            party_size=reservation.party_size,
            special_requests=reservation.special_requests,
            status=reservation.status,
            created_at=reservation.created_at
        )
        
        # Add to database
        self.db.add(db_reservation)
        self.db.commit()
        self.db.refresh(db_reservation)
        
        return self._to_domain(db_reservation)
    
    def delete(self, reservation_id: str) -> bool:
        """Delete a reservation from database"""
        db_reservation = self.db.query(ReservationModel).filter(
            ReservationModel.id == reservation_id
        ).first()
        
        if not db_reservation:
            return False
        
        self.db.delete(db_reservation)
        self.db.commit()
        
        return True
    
    def get_by_restaurant(self, restaurant_id: str) -> List[Reservation]:
        """Get all reservations for a specific restaurant"""
        db_reservations = self.db.query(ReservationModel).filter(
            ReservationModel.restaurant_id == restaurant_id
        ).all()
        
        return [
            self._to_domain(db_res)
            for db_res in db_reservations
        ]
    
    def _to_domain(self, db_reservation: ReservationModel) -> Reservation:
        """Convert database model to domain entity"""
        return Reservation(
            id=db_reservation.id,
            restaurant_id=db_reservation.restaurant_id,
            name=db_reservation.name,
            email=db_reservation.email,
            phone=db_reservation.phone,
            date=db_reservation.date,
            time=db_reservation.time,
            party_size=db_reservation.party_size,
            special_requests=db_reservation.special_requests,
            status=db_reservation.status,
            created_at=db_reservation.created_at
        )

