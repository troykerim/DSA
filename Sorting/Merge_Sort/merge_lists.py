'''
    Leetcode 21 - Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach remaining nodes
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next


def list_to_linkedlist(arr):
    """Convert a Python list into a sorted linked list."""
    if not arr:
        return None
    arr.sort()
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
l1 = list_to_linkedlist([3, 1, 4])
l2 = list_to_linkedlist([2, 5, 6])

merged = mergeTwoLists(l1, l2)
print(linkedlist_to_list(merged))