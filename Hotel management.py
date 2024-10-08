print('\t\t\tWELCOME TO THE HOTEL MASTER NEXUS')
import datetime

# Hotel data (name, available rooms, room price)
hotels = {
    "Hotel PK": {"rooms": 10, "price": 1000},
    "Hotel MSD": {"rooms": 20, "price": 1200},
    "Hotel NBK": {"rooms": 15, "price": 1500},
    "Hotel CBN": {"rooms": 12, "price": 2000},
    "Hotel JSP": {"rooms": 8, "price": 12500}
}

# Booking records
bookings = []

def display_hotels():
    print("Available Hotels:")
    for hotel, data in hotels.items():
        print(f"{hotel}: Rooms available: {data['rooms']}, Price per night: ${data['price']}")

def book_room(hotel_name):
    if hotel_name not in hotels:
        print("Invalid hotel name.")
        return

    if hotels[hotel_name]['rooms'] == 0:
        print("No rooms available in this hotel.")
        return

    name = input("Enter your name: ")
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")
    try:
        check_in_date = datetime.datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.datetime.strptime(check_out, "%Y-%m-%d")
        if check_out_date <= check_in_date:
            print("Invalid dates. Check-out date should be after check-in date.")
            return
    except ValueError:
        print("Invalid date format.")
        return

    nights = (check_out_date - check_in_date).days
    total_price = hotels[hotel_name]['price'] * nights

    print(f"Total price for {nights} nights: ${total_price}")
    confirm = input("Confirm booking (yes/no): ").lower()

    if confirm == 'yes':
        hotels[hotel_name]['rooms'] -= 1
        bookings.append({"hotel": hotel_name, "name": name, "check_in": check_in, "check_out": check_out, "total_price": total_price})
        print("Booking confirmed.")
    else:
        print("Booking cancelled.")

def display_bookings():
    if not bookings:
        print("No bookings yet.")
    else:
        print("Booking Records:")
        for idx, booking in enumerate(bookings, start=1):
            print(f"Booking {idx}:")
            print(f"Hotel: {booking['hotel']}")
            print(f"Name: {booking['name']}")
            print(f"Check-in Date: {booking['check_in']}")
            print(f"Check-out Date: {booking['check_out']}")
            print(f"Total Price: ${booking['total_price']}")

def hotel_management():
    while True:
        print("\nHotel Management :")
        print("1. Display available hotels")
        print("2. Book a room")
        print("3. Display booking records")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_hotels()
        elif choice == '2':
            hotel_name = input("Enter hotel name to book: ")
            book_room(hotel_name)
        elif choice == '3':
            display_bookings()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
hotels={
    "Hotel PK": {"rooms": 10, "price": 100},
    "Hotel MSD": {"rooms": 20, "price": 120},
    "Hotel NBK": {"rooms": 15, "price": 150},
    "Hotel CBN": {"rooms": 12, "price": 200},
    "Hotel JSP": {"rooms": 8, "price": 250}
}
if __name__ == "__main__":
    hotel_management()
