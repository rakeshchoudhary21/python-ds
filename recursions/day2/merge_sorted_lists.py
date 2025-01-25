from LinkedList import Node
# merge two sorted lists into new sorted list
def sort(l1,l2):
    if not l1: return l2
    if not l2: return l1

    if l1.val < l2.val:
        l1.next = sort(l1.next,l2)
        return l1
    else:
        l2.next = sort(l1,l2.next)
        return l2

l1 = Node(2)
l1.next = Node(10)
l1.next.next = Node(12)
l2 = Node(1)
l2.next = Node(11)
l2.next.next = Node(11)
print(sort(l1,l2))