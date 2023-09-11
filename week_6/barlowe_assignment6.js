// Name: Justin Barlowe
// Title: barlowe_assignment6.js
// Description: Assignment 6.2 - Aggregate Queries
// Date: 9/11/2023

// Load houses.js file
load ('houses.js')

// Query to find all houses
db.houses.find()

// Query to find all students
db.students.find()

// Query to add document to the students collection
db.students.insertOne({ firstName: 'Justin', lastName: 'Barlowe', studentId: 's1019', houseId: 'h1010'})

//Query to delete student

db.students.deleteOne({ studentId: 's1019' })

// Query students by house
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house_info"
      }
    }
  ])  


// Query students by house Gryffindor
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house_info"
      }
    },
    {
      $match: { "house_info.houseId": "h1007" }
    }
  ])

// Query students with the Eagle Mascot
db.students.aggregate([
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "house_info"
      }
    },
    {
      $match: { "house_info.mascot": "Eagle" }
    }
  ])
  