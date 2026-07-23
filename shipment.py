from database import connect_database
from tabulate import tabulate
from datetime import date, timedelta

def view_all_shipments():

    connection = connect_database()

    cursor = connection.cursor()

    query = """
    SELECT
    shipment_id,
    customer_id,
    origin,
    destination,
    status,
    shipping_cost
    FROM Shipments
    """

    cursor.execute(query)

    records = cursor.fetchall()

    headers = [
        "Shipment ID",
        "Customer ID",
        "Branch ID",
        "Origin",
        "Destination",
        "Weight",
        "Booking Date",
        "Expected Delivery",
        "Actual Delivery",
        "Status",
        "Shipping Cost"
    ]

    print("\n========== ALL SHIPMENTS ==========\n")

    print(
        tabulate(
            records,
            headers=headers,
            tablefmt="grid"
        )
    )
    cursor.close()
    connection.close()


def search_shipment():
    print("Inside Search Function")

    # Connect to database
    connection = connect_database()
    cursor = connection.cursor()

    # Ask user for shipment ID
    shipment_id = input("Enter Shipment ID: ")

    # SQL Query
    query = """
    SELECT
        s.shipment_id,
        c.customer_name,
        c.phone,
        b.branch_name,
        s.origin,
        s.destination,
        s.weight,
        s.booking_date,
        s.expected_delivery,
        s.actual_delivery,
        s.status,
        s.shipping_cost
    FROM Shipments s
    JOIN Customers c
        ON s.customer_id = c.customer_id
    JOIN Branches b
        ON s.branch_id = b.branch_id
    WHERE s.shipment_id = %s;
    """

    cursor.execute(query, (shipment_id,))

    record = cursor.fetchone()

    if record:

        headers = [
            "Shipment ID",
            "Customer",
            "Phone",
            "Branch",
            "Origin",
            "Destination",
            "Weight",
            "Booking",
            "Expected",
            "Actual",
            "Status",
            "Cost"
        ]

        print("\nShipment Found\n")

        print(tabulate([record], headers=headers, tablefmt="grid"))

    else:

        print("\nShipment Not Found!")





    cursor.close()
    connection.close()



def add_shipment():

    connection = connect_database()
    cursor = connection.cursor()

    print("\n========== ADD NEW SHIPMENT ==========\n")

    # Show available customers
    print("Available Customers")
    cursor.execute("SELECT customer_id, customer_name FROM Customers LIMIT 10")
    customers = cursor.fetchall()

    print(tabulate(customers,
                   headers=["Customer ID", "Customer Name"],
                   tablefmt="grid"))

    customer_id = int(input("\nEnter Customer ID : "))

    # Show available branches
    print("\nAvailable Branches")
    cursor.execute("SELECT branch_id, branch_name FROM Branches")
    branches = cursor.fetchall()

    print(tabulate(branches,
                   headers=["Branch ID", "Branch Name"],
                   tablefmt="grid"))

    branch_id = int(input("\nEnter Branch ID : "))

    origin = input("Enter Origin : ")
    destination = input("Enter Destination : ")

    while origin.lower() == destination.lower():
        print("Origin and Destination cannot be same.")
        destination = input("Enter Destination Again : ")

    weight = float(input("Enter Weight (kg): "))

    # Auto-generated values
    booking_date = date.today()
    expected_delivery = booking_date + timedelta(days=5)

    actual_delivery = None
    status = "Pending"

    shipping_cost = round(weight * 60, 2)

    query = """
    INSERT INTO Shipments
    (
        customer_id,
        branch_id,
        origin,
        destination,
        weight,
        booking_date,
        expected_delivery,
        actual_delivery,
        status,
        shipping_cost
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        customer_id,
        branch_id,
        origin,
        destination,
        weight,
        booking_date,
        expected_delivery,
        actual_delivery,
        status,
        shipping_cost
    )

    cursor.execute(query, values)

    connection.commit()

    print("\nShipment Added Successfully!")
    print("Shipment ID :", cursor.lastrowid)

    cursor.close()
    connection.close()



def update_shipment_status():
    connection = connect_database()
    cursor = connection.cursor()

    shipment_id = input("Enter Shipment ID : ")

    cursor.execute("""
    SELECT shipment_id,status
    FROM Shipments
    WHERE shipment_id=%s
    """,(shipment_id,))

    record = cursor.fetchone()

    if record is None:

        print("\nShipment Not Found!")

        cursor.close()
        connection.close()
        return

    print("\nCurrent Status :",record[1])

    print("\nAvailable Status")

    print("1. Pending")
    print("2. In Transit")
    print("3. Delivered")
    print("4. Cancelled")

    choice=input("\nChoose New Status : ")

    status_map={
        "1":"Pending",
        "2":"In Transit",
        "3":"Delivered",
        "4":"Cancelled"
    }

    if choice not in status_map:

        print("Invalid Choice")

        cursor.close()
        connection.close()
        return

    new_status=status_map[choice]

    if new_status=="Delivered":

        from datetime import date

        actual_delivery=date.today()

    else:

        actual_delivery=None

    cursor.execute("""
    UPDATE Shipments
    SET status=%s,
        actual_delivery=%s
    WHERE shipment_id=%s
    """,(new_status,actual_delivery,shipment_id))

    connection.commit()

    print("\nShipment Updated Successfully!")

    cursor.close()
    connection.close()



def delete_shipment():

    connection = connect_database()
    cursor = connection.cursor()

    shipment_id = input("Enter Shipment ID to Delete : ")

    # Check if shipment exists
    cursor.execute("""
        SELECT shipment_id, status
        FROM Shipments
        WHERE shipment_id = %s
    """, (shipment_id,))

    record = cursor.fetchone()

    if record is None:
        print("\nShipment Not Found!")

        cursor.close()
        connection.close()
        return

    print("\nShipment Found")
    print("Shipment ID :", record[0])
    print("Current Status :", record[1])

    confirm = input("\nAre you sure you want to delete this shipment? (Y/N): ")

    if confirm.upper() != "Y":
        print("\nDeletion Cancelled.")

        cursor.close()
        connection.close()
        return

    cursor.execute("""
        DELETE FROM Shipments
        WHERE shipment_id = %s
    """, (shipment_id,))

    connection.commit()

    print("\nShipment Deleted Successfully!")

    cursor.close()
    connection.close()



def reports_menu():

    while True:

        print("\n")
        print("========== REPORTS ==========")
        print("1. Total Shipments")
        print("2. Shipment Status Report")
        print("3. Branch-wise Shipment Report")
        print("4. Revenue Report")
        print("5. Top Customers")
        print("6. Monthly Shipment Trend")
        print("7. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            total_shipments()

        elif choice == "2":
            print("Coming Soon")

        elif choice == "3":
            print("Coming Soon")

        elif choice == "4":
            print("Coming Soon")

        elif choice == "5":
            print("Coming Soon")

        elif choice == "6":
            print("Coming Soon")

        elif choice == "7":
            break

        else:
            print("Invalid Choice")