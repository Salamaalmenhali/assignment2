# Hotel class manages hotel-level information including name, location, and rooms
class Hotel:
    """Represents the hotel entity."""
    def __init__(self, name, location, phone_number):
        self._name = name  # Hotel name
        self._location = location  # Hotel location
        self._phone_number = phone_number  # Contact number of the hotel
        self._roomsList = []  # List of Room objects

    def setName(self, name):
        self._name = name  # Set hotel name

    def getName(self):
        return self._name  # Return hotel name

    def setLocation(self, location):
        self._location = location  # Set hotel location

    def getLocation(self):
        return self._location  # Return hotel location

    def setPhoneNumber(self, phone_number):
        self._phone_number = phone_number  # Set phone number

    def getPhoneNumber(self):
        return self._phone_number  # Return phone number

    def setRoomsList(self, rooms):
        self._roomsList = rooms  # Set list of rooms

    def getRoomsList(self):
        return self._roomsList  # Return list of rooms

    def displayHotelInfo(self):
        return f"Hotel: {self._name}, Location: {self._location}"  # Return hotel summary


# Room class holds base attributes for any room in the hotel
class Room:
    """Base class for hotel rooms."""
    def __init__(self, room_number, price_per_night, availability_status, amenities):
        self._roomNumber = room_number  # Room number
        self._pricePerNight = price_per_night  # Price per night
        self._availabilityStatus = availability_status  # Room availability status
        self._amenitiesList = amenities  # List of room amenities

    def setRoomNumber(self, room_number):
        self._roomNumber = room_number  # Set room number

    def getRoomNumber(self):
        return self._roomNumber  # Get room number

    def setPricePerNight(self, price):
        self._pricePerNight = price  # Set price per night

    def getPricePerNight(self):
        return self._pricePerNight  # Get price per night

    def setAvailabilityStatus(self, status):
        self._availabilityStatus = status  # Set availability

    def getAvailabilityStatus(self):
        return self._availabilityStatus  # Get availability

    def setAmenitiesList(self, amenities):
        self._amenitiesList = amenities  # Set amenities list

    def getAmenitiesList(self):
        return self._amenitiesList  # Get amenities list

    def calculateCost(self, days):
        return self._pricePerNight * days  # Calculate total cost by multiplying days


# RoomType class inherits Room and adds additional details
class RoomType(Room):
    """Room subclass that includes specific type-related attributes."""
    def __init__(self, room_number, price_per_night, availability_status, amenities, bed_type, max_occupancy, has_balcony, floor_number, view_type):
        super().__init__(room_number, price_per_night, availability_status, amenities)  # Call base Room constructor
        self._bedType = bed_type  # Type of bed
        self._maxOccupancy = max_occupancy  # Maximum occupancy
        self._hasBalcony = has_balcony  # Whether room has balcony
        self._floorNumber = floor_number  # Floor number
        self._viewType = view_type  # Type of view

    def setBedType(self, bed_type):
        self._bedType = bed_type  # Set bed type

    def getBedType(self):
        return self._bedType  # Get bed type

    def setMaxOccupancy(self, max_occupancy):
        self._maxOccupancy = max_occupancy  # Set maximum occupancy

    def getMaxOccupancy(self):
        return self._maxOccupancy  # Get maximum occupancy

    def setHasBalcony(self, status):
        self._hasBalcony = status  # Set balcony status

    def getHasBalcony(self):
        return self._hasBalcony  # Get balcony status

    def setFloorNumber(self, floor_number):
        self._floorNumber = floor_number  # Set floor number

    def getFloorNumber(self):
        return self._floorNumber  # Get floor number

    def setViewType(self, view_type):
        self._viewType = view_type  # Set view type

    def getViewType(self):
        return self._viewType  # Get view type

    def describeRoom(self):
        return f"{self._bedType} bed, View: {self._viewType}"  # Room summary


# Guest class contains guest details and their booking history
class Guest:
    """Represents a hotel guest."""
    def __init__(self, name, contact_info, loyalty_points, booking_history, is_vip):
        self._name = name  # Guest name
        self._contactInfo = contact_info  # Guest contact info
        self._loyaltyPoints = loyalty_points  # Guest loyalty points
        self._bookingHistoryList = booking_history  # Guest's booking history
        self._isVIP = is_vip  # VIP status

    def setName(self, name):
        self._name = name  # Set guest name

    def getName(self):
        return self._name  # Get guest name

    def setContactInfo(self, info):
        self._contactInfo = info  # Set contact info

    def getContactInfo(self):
        return self._contactInfo  # Get contact info

    def setLoyaltyPoints(self, points):
        self._loyaltyPoints = points  # Set loyalty points

    def getLoyaltyPoints(self):
        return self._loyaltyPoints  # Get loyalty points

    def setBookingHistoryList(self, history):
        self._bookingHistoryList = history  # Set booking history

    def getBookingHistoryList(self):
        return self._bookingHistoryList  # Get booking history

    def setVIP(self, status):
        self._isVIP = status  # Set VIP status

    def getVIP(self):
        return self._isVIP  # Get VIP status

    def viewGuestProfile(self):
        return f"Guest: {self._name}, VIP: {self._isVIP}"  # Return guest profile


# Booking class handles reservation details
class Booking:
    """Represents a hotel booking."""
    def __init__(self, booking_id, checkin_date, checkout_date, total_amount, guest_id, room_id):
        self._bookingID = booking_id  # Booking ID
        self._checkInDate = checkin_date  # Check-in date
        self._checkOutDate = checkout_date  # Check-out date
        self._totalAmount = total_amount  # Total cost of booking
        self._guestID = guest_id  # Guest ID associated
        self._roomID = room_id  # Room ID associated

    def setBookingID(self, booking_id):
        self._bookingID = booking_id  # Set booking ID

    def getBookingID(self):
        return self._bookingID  # Get booking ID

    def setCheckInDate(self, date):
        self._checkInDate = date  # Set check-in date

    def getCheckInDate(self):
        return self._checkInDate  # Get check-in date

    def setCheckOutDate(self, date):
        self._checkOutDate = date  # Set check-out date

    def getCheckOutDate(self):
        return self._checkOutDate  # Get check-out date

    def setTotalAmount(self, amount):
        self._totalAmount = amount  # Set total amount

    def getTotalAmount(self):
        return self._totalAmount  # Get total amount

    def setGuestID(self, guest_id):
        self._guestID = guest_id  # Set guest ID

    def getGuestID(self):
        return self._guestID  # Get guest ID

    def setRoomID(self, room_id):
        self._roomID = room_id  # Set room ID

    def getRoomID(self):
        return self._roomID  # Get room ID

    def confirmBooking(self):
        return f"Booking {self._bookingID} confirmed."  # Return confirmation message


# Invoice class represents billing for bookings
class Invoice:
    """Represents the invoice for a booking."""
    def __init__(self, invoice_id, date_issued, tax_amount, discount_applied, booking_id):
        self._invoiceID = invoice_id  # Invoice ID
        self._dateIssued = date_issued  # Date invoice was issued
        self._taxAmount = tax_amount  # Tax amount
        self._discountApplied = discount_applied  # Discount applied
        self._bookingID = booking_id  # Booking ID associated

    def setInvoiceID(self, invoice_id):
        self._invoiceID = invoice_id  # Set invoice ID

    def getInvoiceID(self):
        return self._invoiceID  # Get invoice ID

    def setDateIssued(self, date):
        self._dateIssued = date  # Set issued date

    def getDateIssued(self):
        return self._dateIssued  # Get issued date

    def setTaxAmount(self, tax):
        self._taxAmount = tax  # Set tax

    def getTaxAmount(self):
        return self._taxAmount  # Get tax

    def setDiscountApplied(self, discount):
        self._discountApplied = discount  # Set discount

    def getDiscountApplied(self):
        return self._discountApplied  # Get discount

    def setBookingID(self, booking_id):
        self._bookingID = booking_id  # Set booking ID

    def getBookingID(self):
        return self._bookingID  # Get booking ID

    def generateInvoiceDetails(self):
        return f"Invoice #{self._invoiceID}, Booking: {self._bookingID}"  # Return invoice details


# Feedback class stores guest reviews
class Feedback:
    """Represents feedback left by a guest."""
    def __init__(self, feedback_id, rating, comments, guest_id):
        self._feedbackID = feedback_id  # Feedback ID
        self._rating = rating  # Guest rating
        self._comments = comments  # Guest comments
        self._guestID = guest_id  # Guest ID

    def setFeedbackID(self, feedback_id):
        self._feedbackID = feedback_id  # Set feedback ID

    def getFeedbackID(self):
        return self._feedbackID  # Get feedback ID

    def setRating(self, rating):
        self._rating = rating  # Set rating

    def getRating(self):
        return self._rating  # Get rating

    def setComments(self, comment):
        self._comments = comment  # Set comments

    def getComments(self):
        return self._comments  # Get comments

    def setGuestID(self, guest_id):
        self._guestID = guest_id  # Set guest ID

    def getGuestID(self):
        return self._guestID  # Get guest ID

    def summarizeFeedback(self):
        return f"Rating: {self._rating}, Comment: {self._comments}"  # Return feedback summary
