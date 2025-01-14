

# 0 id obstacle and 1 is ok to go, start at any given random position and reach the bottom right


choices = [
    ['U', -1, 0],
    ['D', 1, 0],
    ['L', 0, -1],
    ['R', 0, 1]
]


def valid(nX, nY,maze):
    if nX <0 or nX >= len(maze) or nY<0 or nY >= len(maze[0]) or maze[nX][nY]==0 : return False
    return True


def rat_in_maze(maze, x, y,path):
    if x+1 == len(maze) and y+1== len(maze[0]):
        print(path)

    for choice in choices:
        nX = x + choice[1]
        nY = y + choice[2] # first item is x and second is y in list, 0th item is direction

        if valid(nX,nY,maze):
            path = path+choice[0]
            maze[x][y] = 0
            rat_in_maze(maze,nX,nY,path)
            path = path[0:-1] # substring sans the last character.
            maze[x][y] = 1



maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

rat_in_maze(maze,0,0, "")





