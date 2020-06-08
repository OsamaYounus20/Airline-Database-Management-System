DROP DATABASE if EXISTS ADMS;
CREATE DATABASE ADMS;
USE ADMS;
DROP TABLE if EXISTS Passenger;
CREATE TABLE Passenger (
    passengerID int NOT NULL AUTO_INCREMENT,
	passport varchar(10),
    FirstName varchar(24)  NOT NULL,
    LastName varchar(24) NOT NULL,
    Address text,
    Sex varchar(8) NOT NULL,
    Phone bigint(11) NOT NULL,
    Age int(3) NOT NULL,
    PRIMARY KEY (passengerID)
);

DROP TABLE if EXISTS Airport;
CREATE TABLE Airport (
	IATA char(3) UNIQUE NOT NULL,
	airportName varchar(255) NOT NULL,
	city varchar(25) NOT NULL,
	country varchar(25) NOT NULL,
	PRIMARY KEY(IATA)
);
DROP TABLE if EXISTS Route;
CREATE TABLE Route (
	routeID int NOT NULL AUTO_INCREMENT,
	depIATA char(3) NOT NULL,
	arrIATA char(3) NOT NULL,
	PRIMARY KEY(routeID),
	FOREIGN KEY(depIATA) REFERENCES airport(IATA),
	FOREIGN KEY(arrIATA) REFERENCES airport(IATA) 
);
DROP TABLE if EXISTS Flight;
CREATE TABLE Flight (
	flightID char(6) NOT NULL UNIQUE,
	routeID int,
	depTime varchar(10),
	depDate varchar(10),
	arrTime varchar(10),
	arrDate varchar(10),
	flightTime varchar(10),
	flightPrice varchar(10),
	PRIMARY KEY(flightID),
	FOREIGN KEY(routeID) REFERENCES Route(routeID)
);
DROP TABLE if EXISTS Booking;
CREATE TABLE Booking (
	pnr char(7) NOT NULL UNIQUE,
	flightID char(6) NOT NULL,
	passengerID int NOT NULL,
	seat_num char(3) NOT NULL,
	class varchar(15) NOT NULL,
	price int NOT NULL,
	PRIMARY KEY(pnr),
	FOREIGN KEY(flightID) REFERENCES Flight(flightID), 
	FOREIGN KEY(passengerID) REFERENCES Passenger(passengerID)
);
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('kh12345678',	'Soha', 'Imran', 'Sharfabad Karachi','F','03001230909',	'21');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('jk23459876','Osama', 'Younus', 'Johar Karachi','M','03019876543','21');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('lr78789898','Aleeha', 'Zafar',	'Bahria Lahore','F','03036654343','22');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('pl97212134','Ayesha', 'Khan','PECHS Karachi','F','03441234567','21');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('hg09914562','Edwin','Van der Saar', 'blue field Holland','M','03332248890','40');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('fh23340987','Harry','Edmund','Liverpool London','M','07769862109','35');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('sk00685489','Tony','Stark','Los Angles USA','M','09826754981','38');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('bt70912087','Christian','Bale','Gotham USA','M','07982345087','41');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('hp78896512','Helena','Carter','Burrow UK','F','06627651239','55');
INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age)   
VALUES ('ru78783109','Natasha ','Romanova','Moscow Russia','F','09210986523','28');

INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('JFK','John F. Kennedy','New York','USA');

INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('KHI','Jinnah International Airport','Karachi','Pakistan');

INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('PHT','Hilo International Airport','Hilo','Hawaii');

INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('CYM','Montreal-Mirabel International Aiport','Quebec','Canada');

INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('SVO','Sheremetyevo International Airport','Moscow','Russia');


INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('LHR','London Heathrow Airport','London','UK');


INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('ATL','Atlanta International','Atlanta','USA');


INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('MAN','Manchester Airport','Manchester','UK');


INSERT INTO Airport (IATA, airportName, city, country)
VALUES ('DXB','Dubai International Airport','Dubai','UAE');

INSERT INTO Airport (IATA, airportName, city, country)
 VALUES ('SIN','Singapore Changi Airport','Changi','Singapore');
INSERT INTO Route (depIATA, arrIATA)
VALUES ('DXB','KHI');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('KHI','MAN');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('SIN','KHI');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('ATL','KHI');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('KHI','LHR');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('KHI','JFK');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('KHI','DXB');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('KHI','PHT');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('CYM','KHI');

INSERT INTO Route (depIATA, arrIATA)
VALUES ('SVO','KHI');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-301','2','06:00:00','2019-09-18','17:00:00','2019-09-18','11:00:00', '32000');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-540','1','13:00:00','2019-09-18','17:30:00','2019-09-18','04:30:00', '88000');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-109','3','11:00:00','2019-09-18','16:00:00','2019-09-18','05:00:00',  '77000');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-202','4','23:00:00','2019-09-18','04:00:00','2019-09-19','05:00:00', '45700');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-701','5','03:00:00','2019-09-18','15:00:00','2019-09-18','12:00:00', '64300');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-999','6','01:00:00','2019-09-18','16:00:00','2019-09-18','16:00:00',  '76500');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-509','7','19:00:00','2019-09-18','23:00:00','2019-09-18','04:00:00', '80000');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-735','8','22:00:00','2019-09-18','11:00:00','2019-09-19','13:00:00', '43000');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-442','9','20:00:00','2019-09-18','19:00:00','2019-09-19','23:00:00', '65000');

INSERT INTO Flight (flightID, routeID, depTime, depDate, arrTime, arrDate, flightTime, flightPrice)
VALUES ('cp-233','10','21:00:00','2019-09-18','06:00:00','2019-09-19','09:00:00', '56095');

INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('6500954','cp-301','5','33A','economy','15000');


INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('5630982','cp-540','2','4A','business','90700');

INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('1239862','cp-109','6','12C','economy','37000');

INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('1009822','cp-666','6','32A','buisness','107000');

INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('3276092','cp-202','4','5E','business','45900');

INSERT INTO Booking (pnr, flightID, passengerID,  seat_num, class, price)
VALUES ('2350934','cp-701','3','7F','business','69202');

INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('7741254','cp-999','7','19B','economy','43887');

INSERT INTO Booking (pnr, flightID, passengerID,  seat_num, class, price)
VALUES ('2120903','cp-509','8','18A','economy','22789');

INSERT INTO Booking (pnr, flightID, passengerID, seat_num, class, price)
VALUES ('5646344','cp-735','1','1F','business','87621');

INSERT INTO Booking (pnr, flightID, passengerID,  seat_num, class, price)
VALUES ('9023923','cp-442','9','17F','economy','64901');

INSERT INTO Booking (pnr, flightID, passengerID,  seat_num, class, price)
VALUES ('6400932','cp-233','10','16D','business','55000');

select * from Passenger;
select * from Airport;
select * from Route;
select * from Flight;
select * from Booking;
