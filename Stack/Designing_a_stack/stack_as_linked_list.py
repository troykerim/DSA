"""
Designing a Stack as a linked list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
    
    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.value)
            curr = curr.next
        return elements

# Testing
stack = Stack()
print("Stack right now: ", stack.display())
print("Is the stack empty? ", stack.isEmpty())

print("\nPushing to the stack\n")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Stack right now: ", stack.display())
print("Stack size check: ", stack.stackSize())
print("Is the stack empty?", stack.isEmpty())
print("Top of the stack: ", stack.peek())

stack.push(5)
stack.push(6)
print("Stack right now: ", stack.display())
print("Stack size check: ", stack.stackSize())

print("\nPopping elements from the stack.\n")
stack.pop()
stack.pop()
stack.pop()

print("Stack right now: ", stack.display())
print("Stack size check: ", stack.stackSize())

stack.pop()
stack.pop()
stack.pop()
print("Stack right now: ", stack.display())
print("Stack size check: ", stack.stackSize())
print("Is the stack empty?", stack.isEmpty())