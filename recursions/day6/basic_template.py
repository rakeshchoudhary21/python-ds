from recursions.day6.Tree import Node
# Trees basic template looks like below

def solve(head:Node):
    #b-c
    if not head or not head.left or not head.right: return head

    # compute for L and R
    L = solve(head.left)
    R = solve(head.right)

    #summarize the result
    return 1+ max(L,R) # something like this.