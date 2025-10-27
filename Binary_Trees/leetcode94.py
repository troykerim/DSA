# class TreeNode:
#     def __init__(self, val = 0, left=None, right=None):
#         self.val = val 
#         self.left = left 
#         self.right = right 

# Recursive Implementation
class Solution:
    def inorderTraversal(self, root):
        res = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
            
        inOrder(root)
        return res
