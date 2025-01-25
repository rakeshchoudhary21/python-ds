
# it's same as josephus problem, actually.

def josephus(kids,k,index):
    if len(kids)==1: return kids[0]
    else:
        index = (index+k-1)% len(kids)
        del kids[index]
        return josephus(kids,k,index)

def winner_of_circular_game(n,k):
    return josephus(list(range(1,n+1)),k,0)


print(winner_of_circular_game(6,5))