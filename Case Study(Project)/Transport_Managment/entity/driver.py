# entity/driver.py
class Driver:
    def __init__(self, DriverID, Name, Status="Available"):
        self.DriverID = DriverID
        self.Name = Name
        self.Status = Status

    def __str__(self):
        return f"DriverID: {self.DriverID}, Name: {self.Name}, Status: {self.Status}"
