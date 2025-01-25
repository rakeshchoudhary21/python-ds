from LinkedList import Node


def swap_in_pairs(l1):
    if not l1 or not l1.next: return l1

    sec = l1.next
    l1.next = swap_in_pairs(sec.next)
    sec.next = l1
    return sec

head = Node(1)
temp = head.add_next(2).add_next(3).add_next(4).add_next(5)
print(head)
print(swap_in_pairs(head))
