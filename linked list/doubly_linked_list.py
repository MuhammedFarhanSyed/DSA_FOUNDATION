class Node:
    def __init__(self ,x):
        self.val=x
        self.right=None
        self.left =None
head = None
tail = None
while True:
    op = int(input("1.insertFirst  2.insertLast  3.Tail_display  4.head_display => "))
    if op == 1:
        # insert at first/starting
        x  = int(input("enter the value => "))
        if not head:
            head = Node(x)
            tail = head
        else:
            temp = Node(x)
            temp.right = head
            head.left = temp
            head =temp
    elif op==2:
        # tail insertion insertion at the end
        x= int(input("enter the value => "))
        if not head:
            head = Node(x)
            tail=head
        else:
            temp = Node(x)
            tail.left = temp
            temp.right = tail
            tail = temp
    elif op==3:
        # traversing from tail 
        curr = tail
        while curr:
            print(curr.val , end=" -> ")
            curr = curr.left
        print()
    elif op == 4:
        curr = head
        # traversing from head
        while curr:
            print(curr.val , end=" -> ")
            curr = curr.left
        print()

