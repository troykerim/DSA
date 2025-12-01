'''
    leetcode 707 - Design Linked List

    Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
    A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
    If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
'''
# Create the LL class
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        # Not required, but a technique to create 2 dummy nodes to help with edge cases!
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left 
        
    # Get the node at some index, first node is at 0th position.  If index DNE, return a default value of -1
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1 
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
        
    # Insert a value at the head of the LL and make it the new head
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node 
        next.prev = node 
        node.next = next
        node.prev = prev
        
    # Insert a value at the tail (end) of the LL and make it the new head
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node 
        next.prev = node 
        node.next = next
        node.prev = prev
    # insert a value at a specific index
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.left.next 
        while cur and index > 0:
            cur = cur.next 
            index -= 1 
        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node 
            next.prev = node 
            node.next = next
            node.prev = prev
        
    # delete a value at a specific index
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur = self.left.next 
        while cur and index > 0:
            cur = cur.next 
            index -= 1 
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev 
            prev.next = next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)