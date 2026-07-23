from shipment import (
    view_all_shipments,
    search_shipment,
    add_shipment,
    update_shipment_status,
    delete_shipment
)
from reports import reports_menu

while True:

    print("\n")

    print("SMART COURIER MANAGEMENT SYSTEM")

    print("----------------------------")

    print("SMART COURIER MANAGEMENT SYSTEM")
    print("--------------------------------")
    print("1. View All Shipments")
    print("2. Search Shipment")
    print("3. Add Shipment")
    print("4. Update Shipment Status")
    print("5. Delete Shipment")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter Choice : ")
    print(choice)

    if choice=="1":
        view_all_shipments()

    elif choice=="2":
        search_shipment()

    elif choice=="3":
        add_shipment()

    elif choice=="4":
        update_shipment_status()

    elif choice=="5":
        delete_shipment()

    elif choice=="6":
        reports_menu()

    elif choice=="7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")