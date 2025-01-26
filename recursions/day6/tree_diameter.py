from recursions.day6.Tree import Node

def tree_diameter(root:Node,res):
    if not root: return 0

    L = tree_diameter(root.left,res)
    R = tree_diameter(root.right,res)

    res[0] = max(res[0],L+R) # check if root may not be part of the diameter.
    return 1+max(L,R) # when path of diameter is thru current root


root = Node(5)
root.left = Node(8)
root.right = Node(6)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(9)
print(root)
res = [0]
tree_diameter(root,res)
print(res)