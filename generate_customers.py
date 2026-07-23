from faker import Faker
import mysql.connector

# Create Faker object for Indian data
fake = Faker("en_IN")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pras#analyst22", 
    database="CourierDB"
)

cursor = connection.cursor()

# Generate 100 Customers
for i in range(100):

    customer_name = fake.name()
    phone = fake.phone_number()[:15]
    email = fake.email()
    city = fake.city()

    sql = """
    INSERT INTO Customers(customer_name, phone, email, city)
    VALUES(%s, %s, %s, %s)
    """

    values = (customer_name, phone, email, city)

    cursor.execute(sql, values)

# Save changes
connection.commit()

print("100 Customers Inserted Successfully!")

cursor.close()
connection.close
