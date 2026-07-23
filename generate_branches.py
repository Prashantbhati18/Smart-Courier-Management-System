# from faker import Faker
# import mysql.connector

# # Create Faker object for Indian data
# fake = Faker("en_IN")

# # Connect to MySQL
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Pras#analyst22", 
#     database="CourierDB"
# )

# cursor = connection.cursor()

# # Generate 100 Customers
# for i in range(100):

#     customer_name = fake.name()
#     phone = fake.phone_number()[:15]
#     email = fake.email()
#     city = fake.city()

#     sql = """
#     INSERT INTO Customers(customer_name, phone, email, city)
#     VALUES(%s, %s, %s, %s)
#     """

#     values = (customer_name, phone, email, city)

#     cursor.execute(sql, values)

# # Save changes
# connection.commit()

# print("100 Customers Inserted Successfully!")

# cursor.close()
# connection.close()

from faker import Faker
import mysql.connector

fake = Faker("en_IN")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pras#analyst22",
    database="CourierDB"
)

cursor = connection.cursor()

branches = [

    ("Delhi Hub","Delhi","Rajesh Kumar"),

    ("Mumbai Hub","Mumbai","Amit Sharma"),

    ("Chandigarh Hub","Chandigarh","Neha Gupta"),

    ("Jaipur Hub","Jaipur","Vikas Singh"),

    ("Lucknow Hub","Lucknow","Rohit Verma"),

    ("Pune Hub","Pune","Pooja Mehta"),

    ("Bangalore Hub","Bangalore","Karan Joshi"),

    ("Hyderabad Hub","Hyderabad","Sneha Reddy"),

    ("Ahmedabad Hub","Ahmedabad","Ankit Patel"),

    ("Kolkata Hub","Kolkata","Priyanka Das")

]

sql = """
INSERT INTO Branches(branch_name, city, manager_name)
VALUES(%s,%s,%s)
"""

for branch in branches:
    cursor.execute(sql, branch)

connection.commit()

print("10 Branches Inserted Successfully!")

cursor.close()
connection.close()