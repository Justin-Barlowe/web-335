# Name: Justin Barlowe
# Title: barlowe-usersp1.py
# Description: Exercise 6.3 - Python with MongoDB, Part 1
# Date: 9/11/2023

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


# Find all users
for user in db.users.find({}):
    print(user)
    breakLine()

# Find user by employeeId
print(db.users.find_one({'employeeId': '1011'}))
breakLine()

# Find user by lastName
print(db.users.find_one({'lastName': 'Mozart'}))
breakLine()
