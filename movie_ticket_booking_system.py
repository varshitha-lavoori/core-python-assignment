total_seats = int(input("total_seats="))
booked_seats = list(map(int, input("booked_seats= ").split()))
book_seat = int(input("book_seat="))
cancel_seat_number = int(input("cancel_seat="))

def booking_seats(total_seats, booked_seats, book_seat):
    if book_seat in booked_seats:
        return
    elif book_seat > total_seats or book_seat < 1:
        return
    else:
        booked_seats.append(book_seat)

def cancel_seat(booked_seats, cancel_seat_number):
    if cancel_seat_number in booked_seats:
        booked_seats.remove(cancel_seat_number)
    else:
        return

def available_seats(total_seats, booked_seats):
    available_seats = [i for i in range(1, total_seats + 1) if i not in booked_seats]
    print(f"Available seats:{available_seats}")

booking_seats(total_seats, booked_seats, book_seat)
cancel_seat(booked_seats, cancel_seat_number)
available_seats(total_seats, booked_seats)
