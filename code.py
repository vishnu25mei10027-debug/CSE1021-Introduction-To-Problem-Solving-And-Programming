# Hotel Management System

rooms = {
    101: {"type": "Single", "price": 1000, "status": "Available"},
    102: {"type": "Double", "price": 1800, "status": "Available"},
    103: {"type": "Suite", "price": 3000, "status": "Available"}
}

customers = {}

def show_rooms():
    print("\nRoom Details:")
    for room, info in rooms.items():
        print("Room No:", room,
              "Type:", info["type"],
              "Price: Rs", info["price"],
              "Status:", info["status"])

def book_room():
    room_no = int(input("Enter room number to book: "))
    if room_no in rooms and rooms[room_no]["status"] == "Available":
        name = input("Enter customer name: ")
        customers[room_no] = name
        rooms[room_no]["status"] = "Booked"
        print("Room booked successfully.")
    else:
        print("Room not available or invalid room number.")

def checkout_room():
    room_no = int(input("Enter room number for checkout: "))
    if room_no in customers:
        print("Customer", customers[room_no], "checked out.")
        del customers[room_no]
        rooms[room_no]["status"] = "Available"
    else:
        print("No booking found for this room.")

def view_bookings():
    print("\nCurrent Bookings:")
    if not customers:
        print("No rooms booked.")
    else:
        for room, name in customers.items():
            print("Room No:", room, "Customer Name:", name)

def main():
    while True:
        print("\nHotel Management System")
        print("1. Show Rooms")
        print("2. Book Room")
        print("3. Checkout Room")
        print("4. View Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            checkout_room()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice.")

main()
