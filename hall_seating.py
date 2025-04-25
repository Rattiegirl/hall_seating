import json
"""
menu()
    show_seats()
    buy_seats()
    search_tickets()
    purchases()

create_seats()

show_seats()
free_seat()
buy_seats()

search_tickets()
purchases()
"""
ROWS = 20
COLS = 26

def create_seats(rows, cols):

    seats = []

    for r in range(rows):
        row = []

        for c in range(cols):
            row.append("a")

        seats.append(row)

    return seats

def show_seats(seats):

    print("Here is what the hall looks like right now:\n")
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    print("\t", end="")
    for i in range(COLS):
        print(alphabet[i], end=" ")
    print("\n")
    num = 0
    for row in seats:
        print(num, end= "\t")
        for col in row:
            print(col, end = " ")
        print()
        num += 1
    
def is_available(seats, row, col, length):

    if (row%2 != 0):
        return False
    if (row < 0 or row > len(seats)):
        return False
    if (col < 0 or col + length > len(seats[row])):
        return False
    for i in range(length):
        if (seats[row][col + i] != "a"):
            return False

    return True

def new_purchase(name, email, row, col, length, total):

    a_purchase = {
        "name": name,
        "email": email,
        "row": row,
        "col": col,
        "length": length,
        "total": total
    }
    purchases = load_pp()

    purchases.append(a_purchase)
    save_pp(purchases)
    print("A purchase has been recorded")

def save_pp(purchases):

    with open("purchases.json", "w") as f:
        json.dump(purchases, f)

def load_pp():

    file_path = "purchases.json"
    try:
        with open(file_path, 'r') as file:
            purchases = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        purchases = []
    return purchases

def receipt(name, email, row, col, length):
    
    base_price = 80
    if (row <= 4):
        base_price = 80
    elif (row <= 10):
        base_price = 50
    elif (row <= 19):
        base_price = 25
    total = (base_price + 5)*length*1.0725

    print("Thank you, " + name + ", for buying tickets worth $" + str(total) + ". We will email a copy of your receipt to " + email + ".")
    new_purchase(name, email, row, col, length, total)
    return total

def reserve_seats(seats, row, col, length):
    if (is_available(seats, row, col, length)):
        for i in range(length):
            seats[row][col + i] = "X"
        for i in range(2):
            if (col - 2 + i >= 0):
                seats[row][col - 2 + i] = "-"
            if (col + length + i <= COLS):
                seats[row][col + length + i] = "-"
        # print("You have reserved the seats")
        return True
    else:
        # print("You didn't reserve the seats")
        return False

def search_tickets(name):

    purchases = load_pp()
    found = False
    for purchase in purchases:
        if purchase["name"] == name:
            print(f"{purchase["name"]} bought ${purchase["total"]} worth of seats. Their email is {purchase["email"]}.\n")
            found = True
    if not found:
        print("There is no purchase with that name")

def show_income():
    file_path = "purchases.json"
    try:
        with open(file_path, 'r') as file:
            purchases = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        purchases = []

    venue_income = 0

    for purchase in purchases:
        print(f"{purchase["name"]} bought ${purchase["total"]} worth of seats. Their email is {purchase["email"]}.\n")
        venue_income += purchase["total"]
    
    print(f"The total income the venue has made is ${venue_income}")

def menu():
    
    welcome_text = """
What would you like to do?

[S]ee the hall
[B]uy seats
[F]ind a ticket
[D]isplay all purchases and total arena income
[Q]uit

"""
    answer = input(welcome_text)

    if answer == "S":

        show_seats(seats)

    elif answer == "B":

        length = int(input("How many seats would you like to buy?\n"))
        place = input("Please enter the starting seat (example 4f)\n")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        row = int(place[:-1])
        col = alphabet.index(place[-1])
        if (reserve_seats(seats, row, col, length)):
            print("You reserved the seats\n")
            name = input("What is the name for the booking?\n")
            email = input("What is your email?\n")
            receipt(name, email, row, col, length)
        else:
            print("You did not reserve the seats\n")

    elif answer == "F":
        name = input("What is the name for the purchase you are trying to find?\n")
        search_tickets(name)
    elif answer == "D":
        show_income()
    elif answer == "Q":
        return False    
    return True

def reserve_previous(seats):
    purchases = load_pp()
    for purchase in purchases:
        reserve_seats(seats, purchase["row"], purchase["col"], purchase["length"])

seats = create_seats(ROWS, COLS)

reserve_previous(seats)
print("Hello! Welcome to the One Direction concert!")
while (menu()):
    pass

