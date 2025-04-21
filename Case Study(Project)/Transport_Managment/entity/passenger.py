# entity/passenger.py
class Passenger:
    def __init__(self, PassengerID=None, FirstName=None, Gender=None, Age=None, Email=None, PhoneNumber=None):
        self.PassengerID = PassengerID
        self.FirstName = FirstName
        self.Gender = Gender
        self.Age = Age
        self.Email = Email
        self.PhoneNumber = PhoneNumber

    def __str__(self):
        return (f"PassengerID: {self.PassengerID}, Name: {self.FirstName}, "
                f"Gender: {self.Gender}, Age: {self.Age}, Email: {self.Email}, Phone: {self.PhoneNumber}")
