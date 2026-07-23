from database import connect_database
from tabulate import tabulate

def total_shipments():
    connection = connect_database()
    cursor = connection.cursor()

    query = """
    SELECT COUNT(*)
    FROM Shipments;
    """

    cursor.execute(query)

    total = cursor.fetchone()[0]

    print("\n========== TOTAL SHIPMENTS ==========\n")
    print("Total Shipments :", total)

    cursor.close()
    connection.close()




def shipment_status_report():

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    SELECT
        status,
        COUNT(*) AS total_shipments
    FROM Shipments
    GROUP BY status
    ORDER BY total_shipments DESC;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    headers = [
        "Shipment Status",
        "Total Shipments"
    ]

    print("\n========== SHIPMENT STATUS REPORT ==========\n")

    print(tabulate(records,
                   headers=headers,
                   tablefmt="grid"))

    cursor.close()
    connection.close()




def branch_wise_report():

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    SELECT
        b.branch_name,
        COUNT(s.shipment_id) AS total_shipments
    FROM Branches b
    JOIN Shipments s
        ON b.branch_id = s.branch_id
    GROUP BY b.branch_name
    ORDER BY total_shipments DESC;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    headers = [
        "Branch Name",
        "Total Shipments"
    ]

    print("\n========== BRANCH-WISE SHIPMENT REPORT ==========\n")

    print(tabulate(records, headers=headers, tablefmt="grid"))

    cursor.close()
    connection.close()



def revenue_report():

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    SELECT
        SUM(shipping_cost),
        AVG(shipping_cost),
        MAX(shipping_cost),
        MIN(shipping_cost)
    FROM Shipments;
    """

    cursor.execute(query)

    record = cursor.fetchone()

    print("\n========== REVENUE REPORT ==========\n")

    print(f"Total Revenue        : ₹ {record[0]:,.2f}")
    print(f"Average Shipping Cost: ₹ {record[1]:,.2f}")
    print(f"Highest Shipping Cost: ₹ {record[2]:,.2f}")
    print(f"Lowest Shipping Cost : ₹ {record[3]:,.2f}")

    cursor.close()
    connection.close()



def top_customers():

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    SELECT
        c.customer_name,
        COUNT(s.shipment_id) AS total_shipments
    FROM Customers c
    JOIN Shipments s
        ON c.customer_id = s.customer_id
    GROUP BY c.customer_name
    ORDER BY total_shipments DESC
    LIMIT 5;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    headers = [
        "Customer Name",
        "Total Shipments"
    ]

    print("\n========== TOP 5 CUSTOMERS ==========\n")

    print(tabulate(records, headers=headers, tablefmt="grid"))

    cursor.close()
    connection.close()




def monthly_shipment_trend():

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    SELECT
        DATE_FORMAT(booking_date,'%Y-%m') AS Month,
        COUNT(*) AS Total_Shipments
    FROM Shipments
    GROUP BY DATE_FORMAT(booking_date,'%Y-%m')
    ORDER BY Month;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    headers = [
        "Month",
        "Total Shipments"
    ]

    print("\n========== MONTHLY SHIPMENT TREND ==========\n")

    print(tabulate(records, headers=headers, tablefmt="grid"))

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
            shipment_status_report()

        elif choice == "3":
            branch_wise_report()

        elif choice == "4":
            revenue_report()

        elif choice == "5":
            top_customers()

        elif choice == "6":
            monthly_shipment_trend()

        elif choice == "7":
            break

        else:
            print("Invalid Choice")