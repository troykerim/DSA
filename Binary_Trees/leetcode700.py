'''
    Leetcode 700
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to insert a value into a BST
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Function to build a BST from a list
def build_bst(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

values = [4, 2, 7, 1, 3]   # elements to insert
val = 2                    # value to search for

root = build_bst(values)   # build the BST
solution = Solution()      # create a Solution object
result = solution.searchBST(root, val)

# Print the result
if result:
    print(f"Found node with value: {result.val}")
else:
    print("Value not found in the BST.")