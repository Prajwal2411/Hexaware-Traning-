# entity/trip.py
class Trip:
    def __init__(self, TripID=None, VehicleID=None, RouteID=None, DepartureDate=None,
                 ArrivalDate=None, Status=None, TripType="Freight", MaxPassengers=0):
        self.TripID = TripID
        self.VehicleID = VehicleID
        self.RouteID = RouteID
        self.DepartureDate = DepartureDate
        self.ArrivalDate = ArrivalDate
        self.Status = Status
        self.TripType = TripType
        self.MaxPassengers = MaxPassengers

    def __str__(self):
        return (f"TripID: {self.TripID}, VehicleID: {self.VehicleID}, RouteID: {self.RouteID}, "
                f"Departure: {self.DepartureDate}, Arrival: {self.ArrivalDate}, Status: {self.Status}")
