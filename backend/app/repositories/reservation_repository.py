"""
Reservation Repository Implementation
Handles data access for reservations
"""
from typing import List, Optional
from app.models import Reservation
import uuid


class IReservationRepository:
    """Interface for reservation repository"""
    
    def get_all(self) -> List[Reservation]:
        """Get all reservations"""
        raise NotImplementedError
    
    def get_by_id(self, reservation_id: str) -> Optional[Reservation]:
        """Get reservation by ID"""
        raise NotImplementedError
    
    def create(self, reservation: Reservation) -> Reservation:
        """Create a new reservation"""
        raise NotImplementedError


class InMemoryReservationRepository(IReservationRepository):
    """
    In-memory implementation of reservation repository
    Stores reservations in memory (data lost on restart)
    """
    
    def __init__(self):
        self._reservations: List[Reservation] = []
    
    def get_all(self) -> List[Reservation]:
        """Get all reservations"""
        return self._reservations.copy()
    
    def get_by_id(self, reservation_id: str) -> Optional[Reservation]:
        """Get reservation by ID"""
        for reservation in self._reservations:
            if reservation.id == reservation_id:
                return reservation
        return None
    
    def create(self, reservation: Reservation) -> Reservation:
        """Create a new reservation"""
        # Generate unique ID if not provided
        if not reservation.id:
            reservation.id = str(uuid.uuid4())[:8]
        
        self._reservations.append(reservation)
        return reservation
    
    def delete(self, reservation_id: str) -> bool:
        """Delete a reservation"""
        initial_length = len(self._reservations)
        self._reservations = [r for r in self._reservations if r.id != reservation_id]
        return len(self._reservations) < initial_length

