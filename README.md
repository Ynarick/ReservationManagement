# Reservation Management - Case of a Land Transport Cooperative

This project aims to develop a reservation management application for a land transport cooperative, specifically for taxi-brousse vehicles. The application will allow customers to book seats and perform various management operations.

## Technologies Used
- Programming Language: Python
- Graphic Library: Tkinter
- Integrated Development Environment (IDE): VSCode
- Database System: MySQL
- Database Server: WampServer

## Project Description
The project involves implementing a reservation management system using a relational database. The main identified entities are as follows:

- CLIENT (Client ID, Name, Address, Hotel Phone)
- VEHICLE (Vehicle ID, Number of Seats, Number of Available Seats)
- RESERVATION (Reservation ID, Departure Date, Reservation Date, Number of Persons, Client ID, Vehicle ID)
- CALENDAR (Departure Date)

The Conceptual Data Schema (CDS) should be developed based on these relationships. To test the functionality of the application, dummy data can be used.

## Key Features of the Application:

1. Updating the number of available seats:
   - Based on the reservations made, the application should automatically update the number of available seats for each vehicle.

2. Generation of reservation invoices:
   - The application should be able to generate detailed invoices for each reservation made by a client.

3. Seat status list:
   - The application should allow viewing the seat status for vehicles that have the same departure. This provides an overview of available and occupied seats.

4. CRUD operations for each file.
