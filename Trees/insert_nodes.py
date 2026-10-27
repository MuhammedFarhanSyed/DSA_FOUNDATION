# inserting array elements into the tree 

a = [2,3,4,5,76,456,53,-25,-345,]

class Node:  
    ''' a class which will create nodes for a tree'''
    def __init__(self ,val):
        self.val = val
        self.right = None
        self.left = None
root = None # starting of a node 

def insert(curr , val):  # a function to insert the values in a tree

    if curr.val < val:
        if not curr.left:
            curr.left = val
        else:
            insert(curr.left , val)
    elif curr.val > val:
        if not curr.right:
            curr.right = val
        else:
            insert(curr.right , val)
    else:
        print(" dublicate value")
# a loop which will iterate over the list and insert values in the tree
for i in a:
    if not root:
        root = Node(i)
    else:
        insert(root , i )
    

