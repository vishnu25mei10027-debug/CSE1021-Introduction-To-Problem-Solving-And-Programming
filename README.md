This project is a basic console-based Hotel Management System written in Python. It lets you manage rooms, handle bookings, checkouts, and view all current reservations through a simple text menu.

Features

1. Show Rooms

Displays all rooms along with:
Room number
Room type (Single / Double / Suite)
Price
Availability status
This helps the user quickly see which rooms are ready to be booked.

2. Book Room

Allows the user to:
Enter a room number
Provide the customer’s name
If the room is available, the system marks it as booked and stores the customer’s details.

3. Checkout Room

Used when a customer leaves.
The system:
Confirms the customer who booked the room
Frees the room
Marks it as available again

4. View Bookings

Shows a list of all rooms that are currently booked along with the customer names.

5. Exit

Closes the program safely.

How It Works

Room details are stored in a dictionary called rooms.
Customer details are stored in another dictionary called customers, where the room number acts as the key.
Each option in the menu calls a specific function to perform its task (show_rooms, book_room, checkout_room, view_bookings).
The program keeps running until the user selects Exit from the menu.

How to Run

1. Make sure Python is installed on your system.
2. Save the script in a file (for example: code.py).
3. Open a terminal or command prompt.
4. Run the script using:
code.py

5. Follow the on-screen menu to use the system.

Notes

This is a simple beginner hotel management project.
Room data resets every time the program restarts, since no database or file storage is used.
You can expand it later by adding features like date-based bookings, billing, or persistent storage.
