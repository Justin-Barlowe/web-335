// Name: Justin Barlowe
// Title: barlowe-assignment4_3.js
// Description: Mongo DB shell queries for week 4 assignment 4.3
// Date: 8/31/2023

// Load users from file
load ('users.js')

// Show all documents in the collection
db.users.find()

// Query to find user with an specific email address
db.users.find({ "email": "jbach@me.com" })

// Query to find a user by last name
db.users.find({ "lastName": "Mozart" })

// Query to find a user by first name
db.users.find({ "firstName": "Richard" })

// Query to find user by employeeId
db.users.find({ "employeeId": "1010" })
