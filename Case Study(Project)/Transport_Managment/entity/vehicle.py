# entity/vehicle.py
class Vehicle:
    def __init__(self, VehicleID=None, Model=None, Capacity=None, Type=None, Status=None):
        self.VehicleID = VehicleID
        self.Model = Model
        self.Capacity = Capacity
        self.Type = Type
        self.Status = Status

    def __str__(self):
        return (f"VehicleID: {self.VehicleID}, Model: {self.Model}, "
                f"Capacity: {self.Capacity}, Type: {self.Type}, Status: {self.Status}")
