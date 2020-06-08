# mycursor.execute("SELECT airlineName FROM Airline;")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# sql_select = "SELECT * FROM T_EMP"
# cur.execute(sql_select)
# for row in cur.fetchall():
#     print("{}, {}, {}, {}".format(row[0], row[1], row[2], row[3]))

# #############################################################
from __future__ import print_function, unicode_literals
import regex
import tabulate
from pprint import pprint
from tabulate import tabulate
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from examples import custom_style_1
from examples import custom_style_2
from datetime import datetime


import mysql.connector

def rec_options(answers):
	if answers['ans'] == 'create a new passenger record':
		while True:
			try:
				p_no = int(input('Enter 10 characters passport number\n'))
			except ValueError:
				print('Not an integer')
				continue;
			else:
				break;
		while len(str(p_no)) != 10:
			print('Enter 10 digits correctly')
			print ('Enter 10 characters passport number')
			p_no = input()
		print('Enter first name')
		fn = input()
		print('Enter last name')
		ln = input()
		print('Enter address')
		ad = input()
		print('enter sex')
		sex = input()
		while True:
			try:
				p = int(input('Enter phone no\n'))
			except ValueError:
				print('Not an integer')
				continue;
			else:
				break;
		while len(str(p)) != 11:
			print('Enter 11 digits correctly')
			print('Enter phone no')
			p = input()

		while True:
			try:
				age = int(input('Enter age\n'))
			except ValueError:
				print('Not an integer')
				continue;
			else:
				break;	
		mycursor = mydb.cursor()
		sql = "INSERT INTO Passenger (passport, FirstName, LastName, Address, Sex, Phone, Age) VALUES('%s','%s','%s','%s','%s', %d,%d);"
		val = (p_no,fn,ln,ad,sex,int(p),int(age))
		mycursor.execute(sql%val)
		mydb.commit()
		mycursor.execute("SELECT * FROM Passenger;")
		myresult = mycursor.fetchall()
		
		print('\t\t\t\t\tPASSENGER RECORD')
		print(tabulate(myresult, headers=['passengerID', 'Passport No.', 'First Name', 'Last Name', 'Address', 'Sex', 'Phone', 'Age'], tablefmt='psql'))
		
				
	elif answers['ans'] == 'update a passenger record':
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Passenger;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\tPASSENGER RECORD')
		print(tabulate(myresult, headers=['passengerID','Passport No.', 'First Name', 'Last Name', 'Address', 'Sex', 'Phone', 'Age'], tablefmt='psql'))
		
		print('Enter the field you want to update')
		field = input()
		print('Enter the value you want to update')
		vals = input()
		print('Enter the passenger ID whose record you want to update')
		pn = input()
		print('Enter updated value')
		uv = input()
		sql = "UPDATE PASSENGER SET %s = '%s'  WHERE passengerID = '%s' AND %s = '%s' ;"
		val = (field, uv, pn, field, vals)
		mycursor.execute(sql%val)
		mydb.commit()
		mycursor.execute("SELECT * FROM Passenger;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\tPASSENGER RECORD')
		print(tabulate(myresult, headers=['passengerID','Passport No.', 'First Name', 'Last Name', 'Address', 'Sex', 'Phone', 'Age'], tablefmt='psql'))
		
	elif answers['ans'] == 'view available flights for a time':

		mycursor = mydb.cursor()
		mycursor.execute("SELECT depIATA, arrIATA from Route;")
		myresult = mycursor.fetchall()
		print('\t\t ROUTE RECORD')
		print(tabulate(myresult, headers=['routeID', 'Departure IATA', 'Arrival IATA'], tablefmt='psql'))

		print('Enter IATA for departure')
		d = input()
		print('Enter IATA for arrival')
		a = input()
		print('Enter start time')
		s = input()
		print('Enter end time')
		e = input()
		
		mycursor = mydb.cursor()
		sql = "SELECT * from Flight WHERE depTime BETWEEN '%s' AND '%s' and flightID = some (SELECT flightID from Flight where routeID = some (SELECT routeID from Route WHERE depIATA = '%s' AND arrIATA = '%s'));"
		val = (s,e,d,a)
		mycursor.execute(sql%val)
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tFLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
		
	elif answers['ans'] == 'generate ticket':
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tFLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Passenger;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\tPASSENGER RECORD')
		print(tabulate(myresult, headers=['passengerID', 'Passsport No.', 'First Name', 'Last Name', 'Address', 'Sex', 'Phone', 'Age'], tablefmt='psql'))
		
		while True:
			try:
				pnr = int(input('Enter PNR\n'))
			except ValueError:
				print('Not an integer')
				continue;
			else:
				break;
		while len(str(pnr)) != 7:
			print('Enter 7 digits correctly')
			print('Enter pnr')
			p = input()
		print('Enter Flight Code')
		fc = input()
		print('Enter PassengerID')
		pid = input()
		print('Enter Seat')
		seat = input()
		print('Enter Class')
		c = input()
		print('Enter Price')
		p = input()

		sql = "INSERT INTO Booking (PNR, flightID, passengerID, seat_num, class, price) VALUES('%s','%s',%d,'%s','%s', %d);"
		val = (pnr, fc, int(pid), seat, c, int(p))

		mycursor.execute(sql%val)
		mydb.commit()
		
		mycursor = mydb.cursor()
		sqls = "SELECT * from Booking WHERE PNR = '%s';"
		vall = (pnr)
		mycursor.execute(sqls%vall)
		myresult = mycursor.fetchall()
		print('\t\t\t\t BOOKING RECORD')
		print(tabulate(myresult, headers=['PNR', 'Flight code', 'Passenger ID','seat number',  'ticket class', 'Price'], tablefmt='psql'))
		

	elif answers['ans'] == 'cheapest flight':
		print('Enter IATA for departure airport')
		d = input()
		print('Enter IATA for arrival airport')
		a = input()
		sql2 = "SELECT routeID from Route WHERE depIATA = '%s' AND arrIATA = '%s';"
		val2 = (d,a)
		mycursor = mydb.cursor()
		mycursor.execute(sql2%val2)
		myresult = mycursor.fetchall()
		route = myresult[0][0]
		route = int(route)
		sql = "SELECT * from Flight WHERE  flightID = some (SELECT flightID from Flight where routeID = some (SELECT routeID from Route WHERE depIATA = '%s' AND arrIATA = '%s'))AND flightPrice = (SELECT min(flightPrice) from Flight where routeID = '%s');" 
		val = (d,a, route)
		mycursor = mydb.cursor()
		mycursor.execute(sql%val)
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tFLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
	elif answers['ans'] == 'history':
		print('Enter passenger ID')
		p = input()
		mycursor = mydb.cursor()
		sql = "SELECT * from Booking where passengerID = %d"
		val = (int(p))
		mycursor.execute(sql%val)
		myresult = mycursor.fetchall()
		print('\t\t\t\t BOOKING RECORD')
		print(tabulate(myresult, headers=['PNR', 'Flight code', 'Passenger ID','seat number',  'ticket class', 'Price'], tablefmt='psql'))
		

	elif answers['ans'] == 'cancel booking':
		print('\nHere are the list of bookings\n')
		print('(pnr, flightID, passengerID, seat, class, price)')
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Booking;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t BOOKING RECORD')
		print(tabulate(myresult, headers=['PNR', 'Flight code', 'Passenger ID','seat number',  'ticket class', 'Price'], tablefmt='psql'))
		
		print ('enter pnr to delete the booking')
		pnr = input()
		mycursor = mydb.cursor()
		sql = "Delete from Booking where pnr = %s"
		mycursor.execute(sql, (pnr,))

		mydb.commit()
		print('\nHere is the updated booking table\n')
		print('(pnr, flightID, passengerID,seat, class, price)')
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Booking;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t BOOKING RECORD')
		print(tabulate(myresult, headers=['PNR', 'Flight code', 'Passenger ID','seat number',  'ticket class', 'Price'], tablefmt='psql'))
		


def admin_options(answers):
	if answers['ans'] == 'create flight record':

		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Route;")
		myresult = mycursor.fetchall()
		
		print('\t\t AVAILABLE ROUTE RECORD')
		print(tabulate(myresult, headers=['routeID', 'Departure IATA', 'Arrival IATA'], tablefmt='psql'))

		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tAVAILABLE FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
			
		print('Enter flight ID')
		f = input()
		print('Enter route ID')
		r = input()
		print('Enter departure time')
		dt = input()
		print('Enter departure date')
		dd = input()
		print('Enter arrival time')
		at = input()
		print('Enter arrival date')
		ad = input()
		print('Enter flight time')
		ft = input()
		print('Enter price')
		pr = input()
		sql = "INSERT INTO Flight VALUES('%s',%d,'%s','%s','%s', '%s','%s', '%s');"
		val = (f,int(r),dt, dd,at,ad,ft,pr)
		mycursor = mydb.cursor()
		mycursor.execute(sql%val)
		mydb.commit()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tUPDATED FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
	
		
	elif answers['ans'] == 'update flight record':
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Flight;")
		myresult = mycursor.fetchall()
		
		print('\t\t\t\t\t\tAVAILABLE FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
		print('enter flight id for which you want to update record')
		fid = input()
		print('enter field you want to update')
		fup = input()
		print('Enter the value you want to update')
		vals = input()
		print('enter new value')
		up = input()
		sql = "UPDATE FLIGHT SET %s = '%s'  WHERE flightID = '%s' AND %s = '%s' ;"
		val = (fup, up, fid, fup, vals)
		mycursor.execute(sql%val)
		mydb.commit()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\tUPDATED FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
	elif answers['ans'] == 'cancel flight':
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tAVAILABLE FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
		print ('enter flightID to delete the flight')
		fid = input()
		mycursor = mydb.cursor()
		sql = "Delete from Booking where flightID = %s"
		mycursor.execute(sql, (fid,))
		mydb.commit()
		sql = "Delete from Flight where flightID = %s"
		mycursor.execute(sql, (fid,))

		mydb.commit()
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * FROM Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tUPDATED FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		

	elif answers['ans'] == 'view arrival departure for an airport':
		print('Enter airport name')
		n = input()
		print('Enter date')
		d = input()

		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Route;")
		myresult = mycursor.fetchall()
		print('\n\t\t ROUTE RECORD')
		print(tabulate(myresult, headers=['routeID', 'Departure IATA', 'Arrival IATA'], tablefmt='psql'))

		sql = "SELECT * FROM Flight WHERE routeID = some (Select routeID FROM Route WHERE depIATA = '%s' AND depDate = '%s');"
		val = (n, d)
		mycursor = mydb.cursor()
		mycursor.execute(sql%val)
		myresult = mycursor.fetchall()
		print('\n\t\t\t\t\t DEPARTING FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time'], tablefmt='psql'))
		
		sql = "SELECT * FROM Flight WHERE routeID = some (Select routeID FROM Route WHERE arrIATA = '%s' AND arrDate = '%s');"
		val = (n,d)
		mycursor = mydb.cursor()
		mycursor.execute(sql%val)
		myresult = mycursor.fetchall()
		print('\n\t\t\t\t\t ARRIVAL FLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time'], tablefmt='psql'))
		

	elif answers['ans'] == 'display tables':
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Route;")
		myresult = mycursor.fetchall()
		print('\t\t ROUTE RECORD')
		print(tabulate(myresult, headers=['routeID', 'Departure IATA', 'Arrival IATA'], tablefmt='psql'))

		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Airport;")
		myresult = mycursor.fetchall()
		print('\t\t\t\tAIRPORT RECORD')
		print(tabulate(myresult, headers=['AirportID', 'Airport Name', 'City', 'Country'], tablefmt='psql'))

		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Passenger;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\tPASSENGER RECORD')
		print(tabulate(myresult, headers=['passengerID', 'Passport No.', 'First Name', 'Last Name', 'Address', 'Sex', 'Phone', 'Age'], tablefmt='psql'))
		
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Flight;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t\t\tFLIGHT RECORD')
		print(tabulate(myresult, headers=['Flight code', 'routeID', 'departure time',  'departure date', 'Arrival time', 'Arrival date', 'Flight time', 'Price'], tablefmt='psql'))
		
		mycursor = mydb.cursor()
		mycursor.execute("SELECT * from Booking;")
		myresult = mycursor.fetchall()
		print('\t\t\t\t BOOKING RECORD')
		print(tabulate(myresult, headers=['PNR', 'Flight code', 'Passenger ID','seat number',  'ticket class', 'Price'], tablefmt='psql'))
		

mydb = mysql.connector.connect(
	database = "ADMS",
	host="localhost",
	user="root",
	passwd="osama"
	)


now = datetime.now()
 
dt = now.strftime("%d/%m/%Y %H:%M:%S")
print('\t\t\t\t\t\t\t\t\tWELCOME TO THE CATHAY PACIFIC\n\n\n\n\t\t\t\t\t\t\t   The current date and time is ',dt)

print('\n\t\t\t\t\t\t\t      Enter A for Administrator R for Receptionist')
str1 = 'A'
str2 = 'R'
inp = input()
if inp == 'A':

	
	questions = [
		{

			'type': 'input',
			'name': 'user',
			'message': 'Enter username',
			'default': 'admin',
		},
		{
			'type': 'password',
			'name': 'last_name',
			'message': 'Enter password',
			'validate': lambda val: val == 'osama' or 'wrong password'
		},
	]

	answers = prompt(questions, style=custom_style_1)
	questions2 = [
	{
		'type': 'list',
		'name': 'ans',
		'message': 'What do you want to do?',
		'choices': [
			'create flight record',
			'update flight record',
			'cancel flight', 
			'view arrival departure for a time',
			'display tables',
		]
	},
	]
	answers2 = prompt(questions2, style=custom_style_1)
	option = admin_options(answers2)
	

elif inp == 'R':

	questions = [
		{
			'type': 'input',
			'name': 'user',
			'message': 'Enter username',
			'default': 'rec',
		},
		{
			'type': 'password',
			'name': 'last_name',
			'message': 'Enter password',
			'validate': lambda val: val == 'younus' or 'wrong password?'
		},
	]
	answers = prompt(questions, style=custom_style_1)
	questions2 = [
	{
		'type': 'list',
		'name': 'ans',
		'message': 'What do you want to do?',
		'choices': [
			'create a new passenger record',
			'update a passenger record',
			'view available flights for a time',
			'generate ticket',
			'cheapest flight',
			'history',
			'cancel booking', 
		]
	},
	]
	answers2 = prompt(questions2, style=custom_style_1)
	option = rec_options(answers2)
	
else: 

	print('wrong option selected')

