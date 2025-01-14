

# given a sudoku, return true if a unique solution exists for the sudoku


def valid(curr, grid, row, col):
    if curr in grid[row]: return False

    for j in range(0,9):
        if grid[j][col] == curr: return False

    rowStart = row - row%3
    colStart = col -col%3

    for i in range(3):
        for j in range(3):
            if grid[i+rowStart][j+colStart] == curr: return False

    return True


def sudoku_solver(grid, row, col):
    if row == 9: return True

    if col == 9:
        return sudoku_solver(grid, row+1, 0) # all cols for given row

    if grid[row][col] > 0 : return sudoku_solver(grid, row, col+1)

    for i in range(1,10):
        if valid(i,grid, row, col):
            grid[row][col] = i
            if sudoku_solver(grid,row,col+1): return True
            grid[row][col] = 0

    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
if sudoku_solver(grid,0,0):
    print(grid)