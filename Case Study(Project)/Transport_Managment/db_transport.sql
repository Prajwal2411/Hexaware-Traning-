create database TransportManagment;

use TransportManagment;

-- Creating of the tables 

--Vehical Table:
create table Vehicles ( 
    VehicleID int primary key identity(1,1),  
    Model varchar(255),
    Capacity decimal(10, 2),
    Type varchar(50),
    Status varchar(50)  
);


-- insert vehicles
INSERT INTO Vehicles (Model, Capacity, Type, Status)
VALUES 
('Tata Bus', 50.00, 'Bus', 'Available'),
('Suzuki Van', 7.50, 'Van', 'In Maintenance'),
('Mahindra Truck', 15.00, 'Truck', 'Available'),
('Volvo Bus', 45.00, 'Bus', 'Allocated'),
('Ashok Leyland Truck', 20.00, 'Truck', 'Available'),
('Maruti Car', 4.00, 'Car', 'Available'),
('Scania Bus', 55.00, 'Bus', 'Allocated'),
('Honda Car', 4.50, 'Car', 'In Maintenance'),
('Hyundai Van', 8.00, 'Van', 'Available'),
('Isuzu Truck', 25.00, 'Truck', 'Allocated');

Select * from Vehicles;

--Routes Table:
create table Routes (
    RouteID int primary key identity(1,1),
    StartDestination varchar(255),
    EndDestination varchar(255),
    Distance decimal(10, 2)
);

--inserting into routes
INSERT INTO Routes (StartDestination, EndDestination, Distance)
VALUES 
('Mumbai', 'Pune', 149.5),
('Delhi', 'Jaipur', 268.2),
('Chennai', 'Bangalore', 345.8),
('Hyderabad', 'Visakhapatnam', 622.3),
('Kolkata', 'Durgapur', 169.7),
('Ahmedabad', 'Surat', 263.1),
('Lucknow', 'Kanpur', 90.6),
('Indore', 'Bhopal', 195.4),
('Chandigarh', 'Amritsar', 228.8),
('Patna', 'Ranchi', 339.9);
--Trips Table:
create table Trips (
    TripID int primary key identity(1,1),
    VehicleID int,
    RouteID int,
    DepartureDate datetime,
    ArrivalDate datetime,
    Status varchar(50),         
    TripType varchar(50) default 'Freight',  
    MaxPassengers int,
    foreign key (VehicleID) references Vehicles(VehicleID),
    foreign key (RouteID) references Routes(RouteID)
);

--Passengers Table:
create table Passengers (
    PassengerID int primary key identity(1,1),
    FirstName varchar(255),
    Gender varchar(255),
    Age int,
    Email varchar(255) unique,
    PhoneNumber varchar(50) -- used varchar because of inclusion of non numberic character like + and () in the number 
);

--Bookings Table:
create table Bookings (
    BookingID int primary key identity(1,1),
    TripID int,
    PassengerID int,
    BookingDate datetime,
    Status varchar(50),         
    foreign key (TripID) references Trips(TripID),
    foreign key (PassengerID) references Passengers(PassengerID)
);


select  @@SERVERNAME;