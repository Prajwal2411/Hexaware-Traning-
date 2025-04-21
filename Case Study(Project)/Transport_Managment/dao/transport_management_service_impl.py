# dao/transport_management_service_impl.py
import pyodbc
from dao.transport_management_service import TransportManagementService
from entity.vehicle import Vehicle
from entity.booking import Booking
from entity.driver import Driver
from util.db_conn_util import DBConnUtil
from exceptions.custom_exceptions import VehicleNotFoundException , BookingNotFoundException


class TransportManagementServiceImpl(TransportManagementService):
    def __init__(self, db_property_file="db.properties"):
        self.conn = DBConnUtil.get_connection(db_property_file)
        self.driver_allocations = {}  # mapping: tripId -> driverId
        # Dummy drivers for simulation; in production use a proper Drivers table.
        self.drivers = [
            Driver(1, "Driver A"),
            Driver(2, "Driver B"),
            Driver(3, "Driver C", Status="On Trip")
        ]

    def addVehicle(self, vehicle: Vehicle) -> bool:
        cursor = self.conn.cursor()
        query = "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (?,?,?,?)"
        try:
            cursor.execute(query, vehicle.Model, vehicle.Capacity, vehicle.Type, vehicle.Status)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in addVehicle:", e)
            return False

    def updateVehicle(self, vehicle: Vehicle) -> bool:
        cursor = self.conn.cursor()
        query = "UPDATE Vehicles SET Model=?, Capacity=?, Type=?, Status=? WHERE VehicleID=?"
        try:
            cursor.execute(query, vehicle.Model, vehicle.Capacity, vehicle.Type, vehicle.Status, vehicle.VehicleID)
            if cursor.rowcount == 0:
                raise VehicleNotFoundException("Vehicle not found with ID " + str(vehicle.VehicleID))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in updateVehicle:", e)
            return False

    def deleteVehicle(self, vehicleId: int) -> bool:
        cursor = self.conn.cursor()
        query = "DELETE FROM Vehicles WHERE VehicleID=?"
        try:
            cursor.execute(query, vehicleId)
            if cursor.rowcount == 0:
                raise VehicleNotFoundException("Vehicle not found with ID " + str(vehicleId))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in deleteVehicle:", e)
            return False

    def getAvailableVehicles(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT VehicleID, Model, Capacity, Type, Status FROM Vehicles WHERE Status = 'Available'"
            cursor.execute(query)
            rows = cursor.fetchall()
            vehicles = []
            for row in rows:
                vehicles.append({"VehicleID": row.VehicleID,"Model": row.Model,"Capacity": row.Capacity,
                    "Type": row.Type,"Status": row.Status })
            return vehicles
        except Exception as e:
            print("Error in getAvailableVehicles:", e)
            return []

    def deallocateVehicle(self, vehicleId):
        try:
            cursor = self.conn.cursor()
            # Update the vehicle status to 'Available'
            query = "UPDATE Vehicles SET Status = 'Available' WHERE VehicleID = ?"
            cursor.execute(query, (vehicleId,))
            self.conn.commit()
            # Check if any row was updated
            if cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error in deallocateVehicle:", e)
            return False
    def scheduleTrip(self, vehicleId: int, routeId: int, departureDate: str, arrivalDate: str) -> bool:
        cursor = self.conn.cursor()
        query = ("INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate, Status, TripType, MaxPassengers) "
                 "VALUES (?,?,?,?,?,?,?)")
        try:
            cursor.execute(query, vehicleId, routeId, departureDate, arrivalDate,
                           "Scheduled", "Freight", 0)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in scheduleTrip:", e)
            return False

    def cancelTrip(self, tripId: int) -> bool:
        cursor = self.conn.cursor()
        query = "UPDATE Trips SET Status='Cancelled' WHERE TripID=?"
        try:
            cursor.execute(query, tripId)
            if cursor.rowcount == 0:
                print("Trip not found with ID", tripId)
                return False
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in cancelTrip:", e)
            return False

    def bookTrip(self, tripId: int, passengerId: int, bookingDate: str) -> bool:
        cursor = self.conn.cursor()
        query = "INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status) VALUES (?,?,?,?)"
        try:
            cursor.execute(query, tripId, passengerId, bookingDate, "Confirmed")
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in bookTrip:", e)
            return False

    def cancelBooking(self, bookingId: int) -> bool:
        cursor = self.conn.cursor()
        query = "UPDATE Bookings SET Status='Cancelled' WHERE BookingID=?"
        try:
            cursor.execute(query, bookingId)
            if cursor.rowcount == 0:
                raise BookingNotFoundException("Booking not found with ID " + str(bookingId))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in cancelBooking:", e)
            return False

    def allocateDriver(self, tripId: int, driverId: int) -> bool:
        driver = next((d for d in self.drivers if d.DriverID == driverId), None)
        if not driver:
            print("Driver not found with ID", driverId)
            return False
        if driver.Status != "Available":
            print("Driver with ID", driverId, "is not available")
            return False
        self.driver_allocations[tripId] = driverId
        driver.Status = "On Trip"
        print(f"Driver {driverId} allocated to Trip {tripId}")
        return True

    def deallocateDriver(self, tripId: int) -> bool:
        if tripId not in self.driver_allocations:
            print("No driver allocated for Trip", tripId)
            return False
        driverId = self.driver_allocations.pop(tripId)
        driver = next((d for d in self.drivers if d.DriverID == driverId), None)
        if driver:
            driver.Status = "Available"
        print(f"Driver {driverId} deallocated from Trip {tripId}")
        return True

    def getAllRoutes(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT RouteID, StartDestination, EndDestination, Distance FROM Routes"
            cursor.execute(query)
            rows = cursor.fetchall()

            routes = []
            for row in rows:
                routes.append({
                    "RouteID": row.RouteID,
                    "StartDestination": row.StartDestination,
                    "EndDestination": row.EndDestination,
                    "Distance": row.Distance
                })
            return routes
        except Exception as e:
            print("Error in getAllRoutes:", e)
            return []
    def getBookingsByPassenger(self, passengerId: int):
        cursor = self.conn.cursor()
        query = "SELECT BookingID, TripID, PassengerID, BookingDate, Status FROM Bookings WHERE PassengerID=?"
        try:
            cursor.execute(query, passengerId)
            rows = cursor.fetchall()
            bookings = []
            for row in rows:
                booking = Booking(BookingID=row.BookingID, TripID=row.TripID,
                                  PassengerID=row.PassengerID, BookingDate=row.BookingDate,
                                  Status=row.Status)
                bookings.append(booking)
            return bookings
        except Exception as e:
            print("Error in getBookingsByPassenger:", e)
            return []

    def getBookingsByTrip(self, tripId: int):
        cursor = self.conn.cursor()
        query = "SELECT BookingID, TripID, PassengerID, BookingDate, Status FROM Bookings WHERE TripID=?"
        try:
            cursor.execute(query, tripId)
            rows = cursor.fetchall()
            bookings = []
            for row in rows:
                booking = Booking(BookingID=row.BookingID, TripID=row.TripID,
                                  PassengerID=row.PassengerID, BookingDate=row.BookingDate,
                                  Status=row.Status)
                bookings.append(booking)
            return bookings
        except Exception as e:
            print("Error in getBookingsByTrip:", e)
            return []



    def getAvailableDrivers(self):
        available_drivers = [d for d in self.drivers if d.Status == "Available"]
        return available_drivers

    def createPassenger(self, FirstName,Gender,Age,PhoneNumber, Email):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Passengers (FirstName,Gender,Age,PhoneNumber, Email)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (FirstName,Gender,Age,PhoneNumber, Email))
            self.conn.commit()

            # Check if the insertion was successful
            if cursor.rowcount > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Error in createPassenger:", e)
            return False

