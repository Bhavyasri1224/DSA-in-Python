class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None


def para(string):
    open_stack = Stack()
    close_stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

 
    for ch in string:
        if ch in "({[":
            open_stack.push(ch)
        elif ch in ")}]":
            close_stack.push(ch)

    while not open_stack.is_empty() and not close_stack.is_empty():
        if open_stack.pop() != pairs[close_stack.pop()]:
            return True

    return open_stack.is_empty() and close_stack.is_empty()

n = input()
if para(n):
    print("Balanced")
else:
    print("Not Balanced")
