# This simple program is created by Dependra Basnet

import random

class Customer:
    def __init__(self, name, phone, address, checkin, checkout, room_type, price, days):
        self.name = name
        self.phone = phone
        self.address = address
        self.checkin = checkin
        self.checkout = checkout
        self.room_type = room_type
        self.price = price
        self.days = days
        self.room_no = random.randrange(20) + 400
        self.customer_id = random.randrange(41) + 300
        self.room_charges = 0
        self.payment_status = False

customers = []

def home():
    print("*WELCOME TO HOTEL THIMPHU")
    print("\t1. Booking")
    print("\t2. Room Information")
    print("\t3. Restaurant")
    print("\t4. Record")
    print("\t5. Payment")
    print("\t6. Discount")
    print("\t7. EXIT")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        booking()
    elif choice == 2:
        room_info()
    # Other menu options should be implemented similarly
    else:
        print("Invalid Choice")

def booking():
    print('Booking Rooms\n')
    name = input('Enter Customer Name: ')
    phone = input('Enter Customer phone: ')
    address = input('Enter Customer address: ')
    checkin = input('Enter Check-In Date [dd-mm-yy]: ')
    checkout = input('Enter Check-Out Date [dd-mm-yy]: ')
    days = int(input("How many nights you want to stay: "))

    print("\n----SELECT ROOM TYPE---")
    print("1. Standard Non-AC  - Nu.3500")
    print("2. Standard AC      - Nu.4000")
    print("3. 3-Bed Non-AC     - Nu.4500")
    print("4. 3-Bed AC         - Nu.5000")
    ch = int(input("--->"))

    if ch == 1:
        room_type = 'Standard Non-AC'
        price = 3500
    # Other room types should be implemented similarly
    else:
        print("Invalid Choice")
        return

    customer = Customer(name, phone, address, checkin, checkout, room_type, price, days)
    customers.append(customer)

    print("\n\t\t\tRoom Booked Successfully")
    print("Room No -", customer.room_no)
    print("Customer ID -", customer.customer_id)

def room_info():
    print('==================Information On Hotels=======================')
    # Display room information
    n = int(input('Press 0 to go back: '))
    if n == 0:
        home()
    else:
        exit()

# Other functions (Restaurant, Record, Payment, Discount) should be implemented similarly

# Main code / driver program
home()
