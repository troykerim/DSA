'''
leetcode 146 - lru cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # Map key to knode
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, next = node.prev, node.next 
        prev.next, next.prev = next, prev
        
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node 
        node.next, node.prev = next, prev
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1 
        
     def put(key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]