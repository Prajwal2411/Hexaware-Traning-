# exception/custom_exceptions.py

class VehicleNotFoundException(Exception):
    """Exception raised when a vehicle is not found in the database."""
    def __init__(self, message="Vehicle not found."):
        self.message = message
        super().__init__(self.message)

class BookingNotFoundException(Exception):
    """Exception raised when a booking is not found in the database."""
    def __init__(self, message="Booking not found."):
        self.message = message
        super().__init__(self.message)
class TripNotFoundException(Exception):
    """Raised when a trip is not found in the database."""
    def __init__(self, message="Trip not found."):
        self.message = message
        super().__init__(self.message)