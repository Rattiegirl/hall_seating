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

def create_seats(rows, cols):

    seats = []

    for r in range(rows):
        row = []

        for c in range(cols):
            row.append("a")

        seats.append(row)

    return seats


def show_seats(seats):

    for row in seats:

        for col in row:

            print(seats[row][col])

    print()
    

def is_available(seats, row, col, length):

    pass

def buy_seats(row, col, length):

    pass

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

        # show_seats(seats)
        pass

    elif answer == "B":

        row = input("What row would you like to buy in?")
        col = input("Which seat would you like to start buying from?")
        length = input("How many seats would you like to buy?")
        buy_seats(row, col, length)

    elif answer == "Q":

        return False    

    return True

while (menu()):
    pass


create_seats(5, 5)
show_seats(seats)
