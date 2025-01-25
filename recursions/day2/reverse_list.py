from LinkedList import Node

# with recursion
def reverse(H):
    if not H or not H.next: return H

    rec = reverse(H.next)
    H.next.next = H
    H.next = None
    return rec

def reverse_iter(H):
    P = None
    C = H
    N = H.next

    while N:
        C.next = P
        P = C
        C = N
        N = N.next

    C.next = P
    print(C)



if __name__=='__main__':
    Head = Node(10)
    Temp = Head.add_next(20).add_next(30).add_next(40).add_next(50)
    r = reverse(Head)
    reverse_iter(r)

