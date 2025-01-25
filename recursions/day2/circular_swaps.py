from LinkedList import Node
import reverse_list
import mid_of_list

# input: 1->2->3->4->5 swap as : 1->5->2->4->3

def circular_swaps(H):
    # find the mid
    mid = mid_of_list.node_before_mid(H)
    mid_start = mid.next
    mid.next = None # decouple the two lists
    # reverse the second half
    reversed_second_half = reverse_list.reverse(mid_start)

    # then join the two list
    f = H
    s = reversed_second_half
    while f and s:
        f_next = f.next
        s_next = s.next
        if f.next:s.next = f.next
        if s: f.next = s
        s = s_next
        f = f_next

    print(H)






head = Node(10)
temp = head.add_next(20).add_next(30).add_next(40).add_next(50).add_next(60)
print(head)
circular_swaps(head)
