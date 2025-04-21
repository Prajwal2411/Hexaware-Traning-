# entity/booking.py
class Booking:
    def __init__(self, BookingID=None, TripID=None, PassengerID=None, BookingDate=None, Status=None):
        self.BookingID = BookingID
        self.TripID = TripID
        self.PassengerID = PassengerID
        self.BookingDate = BookingDate
        self.Status = Status

    def __str__(self):
        return (f"BookingID: {self.BookingID}, TripID: {self.TripID}, PassengerID: {self.PassengerID}, "
                f"BookingDate: {self.BookingDate}, Status: {self.Status}")
