'''
Queue data structure implemented using a linked list

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # Create an empty Queue, similar to writing: self.queue = [] 
        self.front = None
        self.rear = None 
        self.length = 0
        
    # Add a new element at the rear (tail) of the queue.
    def enqueue(self, element):
        new_node = Node(element)
        
         # If the queue is empty 
        if self.rear is None:
            self.front = self.rear = new_node  # front and rear both point to the new node
            self.length += 1 
            return 
        
        # Otherwise, link the new node at the end of the queue
        self.rear.next = new_node   # old rear points to new node
        self.rear = new_node        # move rear to the new node
        self.length += 1 
        
    # This removes an element from the front (head) of the queue.    
    def dequeue(self): 
        # if no elements
        if self.isEmpty():
            return "Queue is empty!"
        
        temp = self.front               # Start at the current front node
        self.front = temp.next          # move front pointer to the next node
        self.length -= 1 
        
        # if the queue became empty
        if self.front is None:          
            self.rear = None            # reset rear as well
            
        return temp.data                # return the removed value
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length 
    
    def printQueue(self):
        temp = self.front 
        while temp:
            print(temp.data, end="")
            temp = temp.next 
        print() 
        
queue = Queue()

queue.enqueue(1)