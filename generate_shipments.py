from faker import Faker
import mysql.connector
import random
from datetime import timedelta

fake = Faker("en_IN")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pras#analyst22",
    database="CourierDB"
)

cursor = connection.cursor()

cities = [
    "Delhi",
    "Mumbai",
    "Pune",
    "Jaipur",
    "Lucknow",
    "Ahmedabad",
    "Hyderabad",
    "Chennai",
    "Bangalore",
    "Chandigarh"
]

status_list = [
    "Delivered",
    "In Transit",
    "Pending",
    "Cancelled"
]

status_weights = [
    60,
    25,
    10,
    5
]

for i in range(500):
    customer_id = random.randint(1,100)
    branch_id = random.randint(1,10)

    origin = random.choice(cities)
    destination = random.choice(cities)

    while origin == destination:
        destination = random.choice(cities)

    weight = round(random.uniform(0.5,25),2)

    booking_date = fake.date_between(
        start_date="-180d",
        end_date="today"
    )

    expected_delivery = booking_date + timedelta(days=random.randint(2,7))

    status = random.choices(
        status_list,
        weights=status_weights,
        k=1
    )[0]

    if status == "Delivered":
        actual_delivery = expected_delivery + timedelta(days=random.randint(-1,3))
    else: 
        actual_delivery = None

    shipping_cost = round(weight * random.randint(40,70),2)

    sql = """
        INSERT INTO Shipments(customer_id, branch_id, origin, destination, weight, booking_date, expected_delivery, actual_delivery, status, shipping_cost)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        customer_id, branch_id, origin, destination, weight, booking_date, expected_delivery, actual_delivery, status, shipping_cost)

    cursor.execute(sql, values)


connection.commit()
print("500 Shipments Inserted Successfully!")
cursor.close()
connection.close()

