
class Node:
    val:int

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.val) + "," + str(self.left)+ "," + str(self.right)
