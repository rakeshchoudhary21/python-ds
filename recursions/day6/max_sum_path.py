from Tree import Node
# path in tree that produces a max sum

def max_sum(root:Node, res):
    if not root: return 0

    L = max_sum(root.left,res)
    R =  max_sum(root.right,res)

    res[0] = max(res[0], L+R+root.val)
    return root.val+max(L,R)


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

res = [0]
max_sum(root,res)
print(res)

