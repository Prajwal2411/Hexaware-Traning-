-- create database
create database OrderManagement;

use OrderManagement;



-- users table

create table Users (
    userid int identity(1,1) primary key,
    username varchar(100) NOT NULL,
    password varchar(100) NOT NULL,
    role varchar(20) NOT NULL,
    constraint chk_users_role check (role IN ('admin', 'user'))
);



-- product table (base product)

create table Product (
    productid int identity(1,1) primary key,
    productname varchar(255) NOT NULL,
    description varchar(MAX),
    price decimal(10, 2) NOT NULL,
    quantityinstock int NOT NULL,
    type varchar(20) NOT NULL,
    constraint chk_product_type check (type IN ('electronics', 'clothing'))
);


-- electronics table (for products of type 'electronics')


create table Electronics (
    productid int primary key,
    brand varchar(100) not null,
    warrantyperiod int not null,  -- represents warranty period in months
    foreign key (productid) references Product(productid)
);


-- clothing table (for products of type 'clothing')

create table Clothing (
    productid int primary key,
    size varchar(50) not null,
    color varchar(50) not null,
    foreign key (productid) references Product(productid)
);


-- orders table

create table Orders (
    orderid int identity(1,1) primary key,
    userid int not null,
    orderdate datetime default getdate(),
    status varchar(50) default 'active',
    foreign key (userid) references Users(userid)
);


-- orderitems table (linking products to orders)

create table OrderItems (
    orderid int not null,
    productid int not null,
    quantity int default 1,
    primary key (orderid, productid),
    foreign key (orderid) references Orders(orderid),
    foreign key (productid) references Product(productid)
);

