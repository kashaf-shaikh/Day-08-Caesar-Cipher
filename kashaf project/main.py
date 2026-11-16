# 🧩 FEATURE 1 — Event Data & Application Setup
print("============== Event Booking System =============")

events = ["DATASCIENCE","IT","CS"]
event_price = [2000,3500,1000]
booking_details = []

booking_should_continue = True
# 🧩 FEATURE 2 — Booking ID Generator
import random
def generate_booking_id():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    numbers = [1,2,3,4,5,6,7,8,9,10]
    booking_id = []
    for i in range(5):
        random_number = str(random.choice(numbers))
        random_character = random.choice(alphabet)
        booking_id.append(random_number)
        booking_id.append(random_character)
    random.shuffle(booking_id)
    book_id = ""
    for idd in booking_id:
        book_id += idd
    return book_id
print(f"Booking ID : {generate_booking_id()}")

# 🧩 FEATURE 3 — Event Selection
# TODO 11: Display all available events with their
index_count = 1
for event,price in (zip(events,event_price)):
    print(f"{index_count}.{event}  Rs{price:,}")
    index_count += 1
    print("\n")

user_choice = int(input("Choose the Event Yo want to Participate 😊?").lower())

if 0 <= user_choice <= 2:
    user_event = events[user_choice - 1]
    ticket_price = event_price[user_choice - 1]
    print(f"Event : {user_event}")
    print(f"Ticket Price: {ticket_price}")

    # 🧩 FEATURE 4 — Customer & Ticket Information
    user_name = input("\nwhat's your name ?").strip().lower()
    user_age = int(input("what's you age ?"))
    no_of_tickets = int(input("How many Ticket You want To Buy ?"))
    total_ticket_price = no_of_tickets * ticket_price
    discount = 0
    if user_age < 18:
        discount = 10
    elif user_age >= 60:
        discount = 15
    else:
        print("Sorry there is no Discount for you 😣!")

    # 🧩 FEATURE 5 — Coupon Code System
    coupon_codes = ["OFF10", "OFF20", "OFF30"]
    coupon_discount = [10, 20, 30]

    have_coupon = input("\nDo you have a 'COUPON CODE😊'Enter it. ?")

    if have_coupon in coupon_codes:
        coupon_code_position = coupon_codes.index(have_coupon)
        discount_per = coupon_discount[coupon_code_position]
        print(f"Discount: {discount_per}")
    else:
        print(f"The coupon is invalid/Don't have a coupon❌")

else:
    print("Please Choose a number from Event Displayed😊\nSelect:")



