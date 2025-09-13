'''
    Leetcode 23 - Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            
            lists = mergedLists

        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


# Helper functions for testing
def list_to_linkedlist(arr):
    """Convert a Python list to a linked list (already sorted)."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(node):
    """Convert a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
s = Solution()

# Example 1: Three lists of different lengths
lists1 = [
    list_to_linkedlist([1, 4, 5]),
    list_to_linkedlist([1, 3, 4]),
    list_to_linkedlist([2, 6])
]
merged1 = s.mergeKLists(lists1)
print(linkedlist_to_list(merged1))  
# Expected: [1, 1, 2, 3, 4, 4, 5, 6]

# Example 2: Lists with single elements
lists2 = [
    list_to_linkedlist([5]),
    list_to_linkedlist([2]),
    list_to_linkedlist([9])
]
merged2 = s.mergeKLists(lists2)
print(linkedlist_to_list(merged2))  
# Expected: [2, 5, 9]

# Example 3: Some lists are empty
lists3 = [
    list_to_linkedlist([]),
    list_to_linkedlist([1, 2, 3]),
    list_to_linkedlist([]),
    list_to_linkedlist([4, 5])
]
merged3 = s.mergeKLists(lists3)
print(linkedlist_to_list(merged3))  
# Expected: [1, 2, 3, 4, 5]

# Example 4: Only one list
lists4 = [
    list_to_linkedlist([10, 20, 30])
]
merged4 = s.mergeKLists(lists4)
print(linkedlist_to_list(merged4))  
# Expected: [10, 20, 30]

# Example 5: All lists empty
lists5 = []
merged5 = s.mergeKLists(lists5)
print(linkedlist_to_list(merged5))  
# Expected: []