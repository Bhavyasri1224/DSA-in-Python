class Node:
  def _init_(self,val):
    self.data=val
    self.next=None
class stack:
  def _init_(self):
    self.top=None
  def push(self,val):
    newnode=Node(val)
    if self.top is None:
      self.top=newnode
    else:
      newnode.next=self.top
      self.top=newnode
  def pop(self):
    if self.top is None:
      print("Stack is Empty")
    poppped=self.top.data
    self.top=self.top.next
    return poppped
  def peek(self):
    if self.top is None:
      print("Stack is empty")
    return self.top.data
  def display(self):
    temp=self.top
    while temp:
      print(temp.data,end="-->")
      temp=temp.next
s=stack()
n=int(input())
for i in range(n):
  k=int(input())
  s.push(k)
s.display()
dele=s.pop()
print("Deleted element",dele)
s.display()
peeek=s.peek()
print("Peek element",peeek)