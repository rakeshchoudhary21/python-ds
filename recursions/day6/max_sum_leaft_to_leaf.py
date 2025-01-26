from Tree import Node
# we need the path to be from leaf node to leaf node only.

def max_sum(root,res):
    if not root: return 0

    L = max_sum(root.left, res)
    R = max_sum(root.right, res)

    temp = max(L,R) + root.val

    # do this only for leaf nodes
    if not root.left and not root.right:
        temp = max(temp, root.val)

    ans = max(temp, L+R+root.val)
    res[0] = max(res[0],ans)
    return ans


root = Node(1)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(8)
root.left.right = Node(-1)
root.right.left = Node(4)
root.right.right = Node(-5)

res = [0]
max_sum(root,res)
print(res)