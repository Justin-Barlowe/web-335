# Name: Justin Barlowe
# Title: barlowe_users2.py
# Description: Assignment 7.3
# Date: 9/18/2023

# Import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@bellevueuniversity.w2mknhu.mongodb.net/web335DB?retryWrites=true&w=majority")

# Connect to database
db = client['web335DB']

# Added line break to make output easier to read
def breakLine():
    print('------------------------')

# Create a new user document
new_user = {
    "first_name": "Justin",
    "last_name": "Barlowe",
    "employeeId": "1014",
    "email": "justin.barlowe@outlook.com"  
}

inserted_user = db.users.insert_one(new_user).inserted_id
print(f"Inserted user: {inserted_user}")


# Display new created user

new_created_user = db.users.find_one({"employeeId": "1014"})
print("New created user: ")
print(new_created_user)

breakLine()

#Update user email address

new_email = "justin.barlowe@proton.me"
db.users.update_one({"employeeId": "1014"}, {"$set": {"email": new_email}})
print(f"Email updated to: {new_email}")

breakLine()

# Display updated user
updated_user = db.users.find_one({"employeeId": "1014"})
print("Updated user: ")
print(updated_user)

breakLine()

# Delete document

db.users.delete_one({"employeeId": "1014"})
print(f"Deleted user: {inserted_user}")

breakLine()

#Prove user was deleted
deleted_user = db.users.find_one({"employeeId": "1014"})    

if deleted_user:
    print("User was not deleted")
else:
    print("User was deleted")

breakLine()