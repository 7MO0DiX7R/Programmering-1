# Create 2 different players and the constants
turn = 0
Player1 = "R"
Player2 = "Y"
ROWS = 6
COLS = 7

# Create a 7x6 board with a indexnumber list for the player to know what to press
def createGrid(rows, cols):
    grid = [["O" for i in range(cols)] for j in range(rows)]
    return grid


def printGrid(grid):
    for row in grid:
        print(*row)


board = createGrid(ROWS, COLS)
indexnumber = ["0", "1", "2", "3", "4", "5", "6"]
print(*indexnumber)
printGrid(board)

# Making a variable to be able to stop the game when someone wins
game_going = True

# looping the whole game so the players can put their coins
while game_going:

    # To make 2 different people play
    if turn % 2 == 0:
        active_player = Player1
    elif turn % 2 == 1:
        active_player = Player2

    # Making the player choose where to place it
    try:
        play = int(input(f"Where do you want to put your coin?({active_player}) "))
        if play >= int(7):
            print("Please choose a number between 0-6")
            continue
        for i in range(1, ROWS + 1):
            if board[ROWS - i][play] == "O":

                board[ROWS - i][play] = active_player
                turn += 1
                break
        print(*indexnumber)
        printGrid(board)
    except ValueError:
        print("You can only choose number between 0-6, letters are not allowed ")
        continue

    # To win vertically or horizontally

    for x in range(ROWS):
        for y in range(COLS):
            if (
                board[x][y]
                == board[x - 1][y]
                == board[x - 2][y]
                == board[x - 3][y]
                == active_player
            ):
                print(f"Congratulation player {active_player}! You win")
                game_going = False
            elif (
                board[x][y]
                == board[x][y - 1]
                == board[x][y - 2]
                == board[x][y - 3]
                == active_player
            ):
                print(f"Congratulation player {active_player}! You win")
                game_going = False
    # To win diagonally
    for x in range(ROWS - 3):
        for y in range(3, COLS):
            if (
                board[x][y] == active_player
                and board[x + 1][y - 1] == active_player
                and board[x + 2][y - 2] == active_player
                and board[x + 3][y - 3] == active_player
            ):
                print(f"Congratulation player ({active_player})! You win")
                game_going = False

    for x in range(ROWS - 3):
        for y in range(COLS - 3):
            if (
                board[x][y] == active_player
                and board[x - 1][y - 1] == active_player
                and board[x - 2][y - 2] == active_player
                and board[x - 3][y - 3] == active_player
            ):
                print(f"Congratulation player ({active_player})! You win")
                game_going = False
