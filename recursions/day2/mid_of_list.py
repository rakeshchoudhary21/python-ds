from LinkedList import Node
# given a list return the node where mid of the list starts


def mid(H):
    sp = H
    fp = H

    while fp and fp.next:
        fp = fp.next.next
        sp = sp.next

    return sp

def node_before_mid(H):
    sp = H
    fp = H
    before_mid = None

    while fp and fp.next:
        fp = fp.next.next
        before_mid = sp
        sp = sp.next

    return before_mid