# tests/test_transport_management.py
import unittest
from dao.transport_management_service_impl import TransportManagementServiceImpl
from entity.vehicle import Vehicle

class TestTransportManagementService(unittest.TestCase):
    def setUp(self):
        self.service = TransportManagementServiceImpl()

    def test_add_vehicle(self):
        vehicle = Vehicle(Model="TestModel", Capacity=20.0, Type="Bus", Status="Available")
        result = self.service.addVehicle(vehicle)
        self.assertTrue(result, "Vehicle should be added successfully.")

    def test_allocate_driver(self):
        tripId = 9999  # Arbitrary tripId for testing allocation logic
        driverId = 1   # Assuming driver with ID 1 is available
        result = self.service.allocateDriver(tripId, driverId)
        self.assertTrue(result, "Driver allocation should return True.")
        # Restore state by deallocating the driver
        self.service.deallocateDriver(tripId)

    def test_delete_vehicle_exception(self):
        result = self.service.deleteVehicle(-1)
        self.assertFalse(result, "Deletion of a non-existent vehicle should fail.")

    def test_add_vehicle(self):
        vehicle = Vehicle(Model="TestModel", Capacity=20.0, Type="Bus", Status="Available")
        result = self.service.addVehicle(vehicle)
        self.assertTrue(result, "Vehicle should be added successfully.")

    def test_allocate_driver(self):
        tripId = 9999  # Arbitrary tripId for testing allocation logic
        driverId = 1  # Assuming driver with ID 1 is available
        result = self.service.allocateDriver(tripId, driverId)
        self.assertTrue(result, "Driver allocation should return True.")
        # Restore state by deallocating the driver
        self.service.deallocateDriver(tripId)

    def test_delete_vehicle_exception(self):
        result = self.service.deleteVehicle(-1)
        self.assertFalse(result, "Deletion of a non-existent vehicle should fail.")

    # Test fetching all routes
    def test_fetch_all_routes(self):
        result = self.service.getAllRoutes()
        self.assertIsInstance(result, list, "Fetching all routes should return a list.")
        self.assertGreater(len(result), 0, "There should be at least one route in the database.")

    # Test creating a booking
    def test_create_booking(self):
        tripId = 1005  # Assuming TripID 1 exists
        passengerId = 1  # Assuming PassengerID 1 exists
        bookingDate = "2025-04-20 10:00:00"
        result = self.service.bookTrip(tripId, passengerId, bookingDate)
        self.assertTrue(result, "Booking should be created successfully.")

    # Test fetching bookings by passenger
    def test_fetch_bookings_by_passenger(self):
        passengerId = 1  # Assuming PassengerID 1 exists
        result = self.service.getBookingsByPassenger(passengerId)
        self.assertIsInstance(result, list, "Fetching bookings by passenger should return a list.")
        self.assertGreater(len(result), 0, "Passenger should have at least one booking.")

    # Test fetching bookings by invalid passenger
    def test_fetch_bookings_by_invalid_passenger(self):
        passengerId = -1  # Invalid PassengerID
        result = self.service.getBookingsByPassenger(passengerId)
        self.assertEqual(len(result), 0, "Fetching bookings by an invalid passenger should return an empty list.")


if __name__ == "__main__":
    unittest.main()
