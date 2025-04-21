# main/main_module.py
import sys
from dao.transport_management_service_impl import TransportManagementServiceImpl
from entity.vehicle import Vehicle


def main():
    service = TransportManagementServiceImpl()
    while True:
        print("\n--- Transport Management System Menu ---")
        print("1. Add Vehicle")
        print("2. Update Vehicle")
        print("3. Delete Vehicle")
        print("4. Show Available Vehicles")
        print("5. Deallocate Vehicle")
        print("6. Show All Routes")
        print("7. Schedule Trip")
        print("8. Cancel Trip")
        print("9. Book Trip")
        print("10. Cancel Booking")
        print("11. Allocate Driver")
        print("12. Deallocate Driver")
        print("13. Get Bookings By Passenger")
        print("14. Get Bookings By Trip")
        print("15. Get Available Drivers")
        print("16. Create Passenger Data")
        print("17. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Model = input("Enter Model: ")
            Capacity = float(input("Enter Capacity: "))
            Type = input("Enter Type: ")
            Status = input("Enter Status: ")
            vehicle = Vehicle(Model=Model, Capacity=Capacity, Type=Type, Status=Status)
            if service.addVehicle(vehicle):
                print("Vehicle added successfully.")
            else:
                print("Failed to add vehicle.")
        elif choice == "2":
            VehicleID = int(input("Enter VehicleID to update: "))
            Model = input("Enter new Model: ")
            Capacity = float(input("Enter new Capacity: "))
            Type = input("Enter new Type: ")
            Status = input("Enter new Status: ")
            vehicle = Vehicle(VehicleID=VehicleID, Model=Model, Capacity=Capacity, Type=Type, Status=Status)
            if service.updateVehicle(vehicle):
                print("Vehicle updated successfully.")
            else:
                print("Failed to update vehicle.")
        elif choice == "3":
            VehicleID = int(input("Enter VehicleID to delete: "))
            if service.deleteVehicle(VehicleID):
                print("Vehicle deleted successfully.")
            else:
                print("Failed to delete vehicle.")
        elif choice == "4":
            vehicles = service.getAvailableVehicles()
            if vehicles:
                for vehicle in vehicles:
                    print(f"Vehicle ID: {vehicle['VehicleID']}, Model: {vehicle['Model']}, "
                          f"Capacity: {vehicle['Capacity']}, Type: {vehicle['Type']}, Status: {vehicle['Status']}")
            else:
                print("No available vehicles found.")
        elif choice == "5":
            vehicleId = int(input("Enter VehicleID to deallocate: "))
            if service.deallocateVehicle(vehicleId):
                print(f"Vehicle with ID {vehicleId} deallocated successfully.")
            else:
                print(f"Failed to deallocate vehicle with ID {vehicleId}.")
        elif choice == "6":  # Show All Routes Option
            routes = service.getAllRoutes()
            if routes:
                for route in routes:
                    print(f"Route ID: {route['RouteID']}, Start: {route['StartDestination']}, "
                          f"End: {route['EndDestination']}, Distance: {route['Distance']} km")
            else:
                print("No routes found.")
        elif choice == "7":
            vehicleId = int(input("Enter VehicleID: "))
            routeId = int(input("Enter RouteID: "))
            departureDate = input("Enter Departure Date (YYYY-MM-DD HH:MM:SS): ")
            arrivalDate = input("Enter Arrival Date (YYYY-MM-DD HH:MM:SS): ")
            if service.scheduleTrip(vehicleId, routeId, departureDate, arrivalDate):
                print("Trip scheduled successfully.")
            else:
                print("Failed to schedule trip.")
        elif choice == "8":
            tripId = int(input("Enter TripID to cancel: "))
            if service.cancelTrip(tripId):
                print("Trip cancelled successfully.")
            else:
                print("Failed to cancel trip.")
        elif choice == "9":
            tripId = int(input("Enter TripID: "))
            passengerId = int(input("Enter PassengerID: "))
            bookingDate = input("Enter Booking Date (YYYY-MM-DD HH:MM:SS): ")
            if service.bookTrip(tripId, passengerId, bookingDate):
                print("Trip booked successfully.")
            else:
                print("Failed to book trip.")
        elif choice == "10":
            bookingId = int(input("Enter BookingID to cancel: "))
            if service.cancelBooking(bookingId):
                print("Booking cancelled successfully.")
            else:
                print("Failed to cancel booking.")
        elif choice == "11":
            tripId = int(input("Enter TripID: "))
            driverId = int(input("Enter DriverID to allocate: "))
            if service.allocateDriver(tripId, driverId):
                print("Driver allocated successfully.")
            else:
                print("Failed to allocate driver.")
        elif choice == "12":
            tripId = int(input("Enter TripID to deallocate driver: "))
            if service.deallocateDriver(tripId):
                print("Driver deallocated successfully.")
            else:
                print("Failed to deallocate driver.")
        elif choice == "13":
            passengerId = int(input("Enter PassengerID: "))
            bookings = service.getBookingsByPassenger(passengerId)
            if bookings:
                for booking in bookings:
                    print(booking)
            else:
                print("No bookings found for this passenger.")
        elif choice == "14":
            tripId = int(input("Enter TripID: "))
            bookings = service.getBookingsByTrip(tripId)
            if bookings:
                for booking in bookings:
                    print(booking)
            else:
                print("No bookings found for this trip.")
        elif choice == "15":
            drivers = service.getAvailableDrivers()
            if drivers:
                for driver in drivers:
                    print(driver)
            else:
                print("No available drivers.")
        elif choice == "16":  # Create Passenger Data Option
            FirstName = input("Enter Passenger Name: ")
            Gender = input("Enter Passenger Gender: ")
            Age = int(input("Enter Passenger age:"))
            PhoneNumber = input("Enter Contact Number: ")
            Email = input("Enter Email Address: ")
            if service.createPassenger(FirstName,Gender,Age,PhoneNumber, Email):
                print("Passenger data created successfully.")
            else:
                print("Failed to create passenger data.")
        elif choice == "17":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    service.conn.close()


if __name__ == "__main__":
    main()
