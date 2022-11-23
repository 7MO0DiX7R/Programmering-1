def createGrid(rows, cols):
    grid = [["O" for i in range(cols)] for j in range(rows)]
    return grid


def printGrid(grid):
    for row in grid:
        print(*row)


board = createGrid(6, 7)
printGrid(board)
