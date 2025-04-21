# dao/transport_management_service.py
from abc import ABC, abstractmethod

class TransportManagementService(ABC):
    @abstractmethod
    def addVehicle(self, vehicle) -> bool:
        pass

    @abstractmethod
    def updateVehicle(self, vehicle) -> bool:
        pass

    @abstractmethod
    def deleteVehicle(self, vehicleId: int) -> bool:
        pass

    @abstractmethod
    def scheduleTrip(self, vehicleId: int, routeId: int, departureDate: str, arrivalDate: str) -> bool:
        pass

    @abstractmethod
    def cancelTrip(self, tripId: int) -> bool:
        pass

    @abstractmethod
    def bookTrip(self, tripId: int, passengerId: int, bookingDate: str) -> bool:
        pass

    @abstractmethod
    def cancelBooking(self, bookingId: int) -> bool:
        pass

    @abstractmethod
    def allocateDriver(self, tripId: int, driverId: int) -> bool:
        pass

    @abstractmethod
    def deallocateDriver(self, tripId: int) -> bool:
        pass

    @abstractmethod
    def getBookingsByPassenger(self, passengerId: int):
        pass

    @abstractmethod
    def getBookingsByTrip(self, tripId: int):
        pass

    @abstractmethod
    def getAvailableDrivers(self):
        pass


    def createPassenger(self, PassengerName, ContactNumber, EmailAddress):
        pass