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

    if (row < 0 or row > len(seats)):

        return False

    if (col < 0 or col + length > len(seats[row])):

        return False

    for i in range(length):

        if (seats[row][col + i] != "a"):

            return False

    return True

def buy_seats(seats, row_num, col_num, length):
    row = row_num -1
    col = col_num -1
    if (is_available(seats, row, col, length)):
        for i in range(length):
            seats[row][col + i] = "X"
        print("YOU BOUGHT A SEET")
    else:
        print("YOU NO BOUGHT A SEET")

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
[Q]uit

"""
    answer = input(welcome_text)

    if answer == "S":

        show_seats(seats)

    elif answer == "B":

        row_num = int(input("What row would you like to buy in?\n"))
        col_num = int(input("Which seat would you like to start buying from?\n"))
        length = int(input("How many seats would you like to buy?\n"))
        buy_seats(seats, row_num, col_num, length)

    elif answer == "Q":

        return False    

    return True



seats = create_seats(ROWS, COLS)


while (menu()):
    pass

