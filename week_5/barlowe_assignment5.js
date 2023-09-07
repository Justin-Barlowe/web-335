// Name: Justin Barlowe
// Title: barlowe-assignment5.3.js
// Description: Mongo DB queries for week 4 assignment 5.2
// Date: 9/7/2023

//Create new user
db.users.insertOne({ "firstName": "Joseph", "lastName": "Haydn", "employeeId": "1013", "email": "jhadyn@me.com"
, "dateCreated": new Date() })

//Update Mozart's email
db.users.updateOne({ "lastName: "Mozart" }, { $set: { "email": "mozart@me.com" } } )
)

// Find users using projection
db.users.find({}, { firstName: 1, lastName: 1, email: 1})

