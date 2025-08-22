class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue: ", queue.queue)

print("Dequeue: ", queue.dequeue())

print("Peek: ", queue.peek())

print("isEmpty: ", queue.isEmpty())

print("Size: ", queue.size())
print()
print("Queue: ", queue.queue)
queue.dequeue()
print("Queue: ", queue.queue)
queue.dequeue()
print("Queue: ", queue.queue)
print("isEmpty: ", queue.isEmpty())
print("Size: ", queue.size())