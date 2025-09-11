class Node:
  def __init__(self,val):
    self.data = val
    self.next = None
class Linkedlist:
  
  def __init__(self):
    self.head = None
    
  def insert(self,val):
    
    newnode = Node(val)
    
    if self.head is None:
      self.head = newnode
      
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
        
      temp.next = newnode
      
  def display(self):
    
    if self.head is None:
      print("Linkedlist is Empty")
    
    temp = self.head
    while temp is not None:
      print(temp.data,end="-->")
      temp = temp.next
    print("Null")
      
list1 = Linkedlist()

n = int(input())
for i in range(n):
  val = int(input())
  list1.insert(val)
  
list1.display()