from LinkedList import Node
# remove nodes that have any node gt then it on the right

def remove_smaller_nodes(H):
    if H is None: return None

    H.next = remove_smaller_nodes(H.next)
    if H.next is not None and H.val < H.next.val: return H.next
    else: return H


Head = Node(1)
temp = Head.add_next(0).add_next(5).add_next(2).add_next(3).add_next(1)
print(Head)
res = remove_smaller_nodes(Head)
print(res)
