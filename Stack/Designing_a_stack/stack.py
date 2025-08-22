"""
Designing a Stack

"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


stack = Stack()
print("Stack right now: ", stack.stack)
print("Is the stack empty? ", stack.isEmpty())

print("\nPushing to the stack\n")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Stack right now: ", stack.stack)
print("Stack size check: ", stack.size())
print("Is the stack empty?", stack.isEmpty())
print("Top of the stack: ", stack.peek())

stack.push(5)
stack.push(6)
print("Stack right now: ", stack.stack)
print("Stack size check: ", stack.size())

print("\nPopping elements from the stack.\n")
stack.pop()
stack.pop()
stack.pop()

print("Stack right now: ", stack.stack)
print("Stack size check: ", stack.size())
stack.pop()
stack.pop()
stack.pop()
print("Stack right now: ", stack.stack)
print("Stack size check: ", stack.size())