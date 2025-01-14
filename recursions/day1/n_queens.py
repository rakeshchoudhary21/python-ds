

# place the queen appropriately on a given board
# since a chess board is a square so we don't need row and col both

def valid(row, col, board):
    if 'Q' in board[row] : return False # already a queen in row

    for j in range(len(board)):
        if board[j][col] == 'Q' : return False # col

    # corner diagonal left upper side
    k = row
    j= col
    while k>=0 and j>=0:
        if board[k][j]=='Q': return False
        k-=1
        j-=1

    # corner diagonal left downside
    k = row
    j= col
    while k<len(board) and j>0:
        if board[k][j]=='Q' : return False
        k+=1
        j-=1

    # it's safe to place the Queen
    return True

# this solution prints all the possible results
# the way the valid func is written thats why we are going just col by col
# since filling is col by col so we can assume that only left side column is filled yet.
def n_queens(board, col, N):
    if col == N:
        print(board)
        return

    for row in range(N):
        if valid(row, col, board):
            board[row][col] = 'Q'
            n_queens(board,col+1, N)
            board[row][col] = '.'

board = [['.','.','.','.'],
        ['.','.','.','.'],
        ['.','.','.','.'],
        ['.','.','.','.']]

n_queens(board,0,4)