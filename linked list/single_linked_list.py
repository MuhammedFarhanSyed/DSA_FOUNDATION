class Node:
  def __init__(self , x):
    self.val = x
    self.next = None
head = None
tail = None
while True:
  ch = int(input(" 1.insert  2.display  3 . exit  => "))
  if ch ==1:
    x = int(input('enter the value to insert => '))
    if not head:
      head = Node(x)
      tail = head
    else:
      tail.next = Node(x)
      tail=tail.next
  elif ch==2:
    curr = head
    while curr:
      print(curr.val , end=" -> ")
      curr = curr.next
    print()
  else:
    print("exited ...")
    break