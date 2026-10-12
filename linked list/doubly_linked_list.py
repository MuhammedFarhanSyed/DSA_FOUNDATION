class Node:
    def __init__(self ,x):
        self.val=x
        self.right=None
        self.left =None
head = None
tail = None
while True:
    op = int(input("1.insertFirst  2.insertLast  3.display => "))
    if op == 1:
        x  = int(input("enter the value => "))
        if not head:
            head = Node(x)
            tail = head
        else:
            temp = Node(x)
            temp.right = head
            head.left = temp
            head =temp
    elif op==3:
        curr = head
        while curr:
            print(curr.val , end=" -> ")
            curr = curr.next
        print()
