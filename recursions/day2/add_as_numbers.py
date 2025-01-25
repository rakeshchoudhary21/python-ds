from LinkedList import Node
# add lists like decimal numbers

def add(l1, l2, carry: int, res):
    if not l1 and not l2:
        if carry > 0: res.next = Node(carry)
        return

    if l1 is None:
        val = int((l2.val+carry)%10)
        carry = int((l2.val+carry) / 10)
        res.next = Node(val)
        add(l1,l2.next, carry,res.next)
    if l2 is None:
        val = int((l1.val + carry) % 10)
        carry = int((l1.val + carry) / 10)
        res.next = Node(val)
        add(l1.next, l2, carry, res.next)
    if l1 and l2:
        val = int((l1.val+l2.val + carry) % 10)
        carry = int((l1.val+l2.val + carry) / 10)
        res.next = Node(val)
        add(l1.next, l2.next, carry, res.next)


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(41)
res = Node(0)
add(l1,l2,0, res)
print(res.next)