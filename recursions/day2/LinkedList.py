class Node:
    val: int

    def __init__(self,val):
        self.val = val
        self.next = None

    def add_next(self,val):
        self.next = Node(val)
        return self.next

    def __str__(self):
       return str(self.val) +"->"+ str(self.next)

