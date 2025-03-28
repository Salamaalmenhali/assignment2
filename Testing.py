from datetime import datetime
from ProgramFundamentalsAssignment2 import Hotel, RoomType, Guest, Booking, Invoice, Feedback

# ------------------ Setup Hotel & Rooms ------------------

# Create a hotel instance
hotel = Hotel("Royal Stay", "UAE", "+971-123-5678")

# Create two room instances with their respective details
room1 = RoomType("101", 120.0, True, ["swimming pool", "gym"], "Queen", 2, True, 1, "Garden")
room2 = RoomType("103", 90.0, True, ["spa"], "Single", 1, False, 1, "Street")

# Add the rooms to the hotel's room list
hotel.setRoomsList([room1, room2])

# ------------------ Display Full Hotel Info ------------------

# Display hotel basic information
print("\n--- HOTEL DETAILS ---")
print(f"Hotel Name: {hotel.getName()}")
print(f"Location: {hotel.getLocation()}")
print(f"Phone: {hotel.getPhoneNumber()}")

# Display information about all rooms
print("\n--- ROOMS INFO ---")
for room in hotel.getRoomsList():
    print(f"Room Number: {room.getRoomNumber()}")
    print(f"  Bed Type: {room.getBedType()}")
    print(f"  Price/Night: {room.getPricePerNight()}")
    print(f"  Max Occupancy: {room.getMaxOccupancy()}")
    print(f"  Has Balcony: {room.getHasBalcony()}")
    print(f"  Floor: {room.getFloorNumber()}")
    print(f"  View: {room.getViewType()}")
    print(f"  Amenities: {room.getAmenitiesList()}")
    print(f"  Available: {room.getAvailabilityStatus()}")
    print("---------------")

# ------------------ Guest Creation ------------------

# Prompt user to create a guest account
print("\n--- CREATE GUEST ACCOUNT ---")
name = input("Enter your name: ")  # Example: Alice Kim
email = input("Enter your email: ")  # Example: alice@example.com
contact = input("Enter your phone number: ")  # Example: +971-555-9999
points = int(input("Enter your loyalty points: "))  # Example: 4
vip_input = input("Are you a VIP guest? (yes/no): ").lower()
is_vip = vip_input == "yes"  # Convert to boolean

# Create the guest object using provided information
guest = Guest(name, f"{email} | {contact}", points, [], is_vip)

# Display guest details
print("\nGuest Created:")
print(f"Name: {guest.getName()}")
print(f"Email/Contact: {guest.getContactInfo()}")
print(f"Loyalty Points: {guest.getLoyaltyPoints()}")
print(f"VIP: {guest.getVIP()}")

# ------------------ Room Search ------------------

# Allow user to search for rooms based on an amenity
print("\n--- ROOM AMENITY SEARCH ---")
desired = input("Search for an amenity (swimming pool, gym, spa): ").lower()
found = False

# Search all rooms for the entered amenity
for room in hotel.getRoomsList():
    if desired in [a.lower() for a in room.getAmenitiesList()]:
        print(f"Room {room.getRoomNumber()} includes {desired}")
        found = True

# If no matching rooms found
if not found:
    print("No rooms found with that amenity.")

# ------------------ Make Reservation ------------------

# Begin reservation process
print("\n--- MAKE A RESERVATION ---")
room_num = input("Enter room number to reserve: ")  # Example: 101
checkin = input("Enter check-in date (YYYY-MM-DD): ")  # Example: 2025-04-10
checkout = input("Enter check-out date (YYYY-MM-DD): ")  # Example: 2025-04-14

# Get the selected room object
selected_room = next((r for r in hotel.getRoomsList() if r.getRoomNumber() == room_num), None)

# Calculate number of nights
days = (datetime.strptime(checkout, "%Y-%m-%d") - datetime.strptime(checkin, "%Y-%m-%d")).days

# If a valid room is selected
if selected_room:
    # Calculate total cost and create booking
    cost = selected_room.calculateCost(days)
    booking = Booking("B100", checkin, checkout, cost, guest.getName(), room_num)

    # Update room availability and guest history
    guest.setBookingHistoryList([booking])
    selected_room.setAvailabilityStatus(False)

    # Display confirmation details
    print("\nBooking Confirmed:")
    print(f"Guest: {guest.getName()}")
    print(f"Room: {room_num}")
    print(f"Stay: {checkin} to {checkout} ({days} nights)")
    print(f"Total Cost: {cost}")

    # ------------------ Invoice ------------------

    # Generate and display invoice
    invoice = Invoice("INV100", datetime.now().strftime("%Y-%m-%d"), 15.0, 5.0, booking.getBookingID())
    print("\n--- INVOICE ---")
    print(invoice.generateInvoiceDetails())

    # ------------------ Feedback ------------------

    # Collect and display feedback
    print("\n--- LEAVE FEEDBACK ---")
    rating = int(input("Rate your stay (1-5): "))  # Example: 4
    comment = input("Write a short comment: ")  # Example: Amazing location and spa!
    feedback = Feedback("F100", rating, comment, guest.getName())
    print("\nFeedback Received:")
    print(feedback.summarizeFeedback())

    # ------------------ View Booking History ------------------

    # Show all past bookings for the guest
    print("\n--- YOUR BOOKING HISTORY ---")
    for b in guest.getBookingHistoryList():
        print(f"{b.getBookingID()} | Room {b.getRoomID()} | {b.getCheckInDate()} to {b.getCheckOutDate()}")

    # ------------------ Cancel Option ------------------

    # Offer cancellation option
    cancel = input("\nDo you want to cancel your reservation? (yes/no): ").lower()
    if cancel == "yes":
        selected_room.setAvailabilityStatus(True)
        print(f"Booking cancelled. Room {room_num} is now available again.")
    else:
        print("Booking remains confirmed.")

# If invalid room entered
else:
    print("Room not found or invalid number.")

