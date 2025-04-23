# """
# This example code creates a 2d list (2d matrix) that can store seating.
# The matrix is populated with . since all seats are available
# """
# # our test matrix has 4 rows and 10 columns
# N_ROW = 20
# N_COL = 26

# # available seat

# available_seat = 'a'

# # create some available seating

# seating = []
# for r in range(N_ROW):
#     row = []

#     for c in range(N_COL):
#         row.append(available_seat)
#     seating.append(row)

# seating[15][15] = "X"

# # print available seating
# for r in range(N_ROW):
#     print(r+1, end="\t")

#     for c in range(N_COL):
#         print(seating[r][c], end=" ")
#     print()


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

    print("Here is what the hall looks like right now:")

    for row in seats:

        for col in row:

            print(col, end = " ")

        print()
    

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


def receipt(name, email, row, length):
    
    base_price = 80
    if (row <= 4):
        base_price = 80
    elif (row <= 10):
        base_price = 50
    elif (row <= 19):
        base_price = 25
    total = (base_price + 5)*length*1.0725

    print("Thank you, " + name + ", for buying tickets worth $" + str(total) + ". We will email a copy of your receipt to " + email + ".")
    return total
    



def reserve_seats(seats, row, col, length):
    if (is_available(seats, row, col, length)):
        for i in range(length):
            seats[row][col + i] = "X"
        for i in range(length + 2):
            seats[row + 1][col + i - 1] = "-"
            seats[row - 1][col + i - 1] = "-"
        for i in range(2):
            seats[row][col - 2 + i] = "-"
            seats[row][col + length + i] = "-"
        print("You have reserved the seats")
        return True
    else:
        print("You didn't reserve the seats")
        return False


def search_tickets(name):

    pass

def purchases():

    pass

def menu():
    
    welcome_text = """
Hello! What would you like to do?

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
        row = int(place[0])
        col = alphabet.index(place[1])
        if (reserve_seats(seats, row, col, length)):
            name = input("What is the name for the booking?\n")
            email = input("What is your email?\n")
            total_price = receipt(name, email, row, length)
            


    elif answer == "Q":

        return False    

    return True



seats = create_seats(ROWS, COLS)


while (menu()):
    pass

