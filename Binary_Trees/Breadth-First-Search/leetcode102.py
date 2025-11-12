'''
    Leetcode 102 - Binary Tree Level Order Traversal
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
import collections
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class solution:
    def levelOrder(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            levels = []
            for i in range(qlen):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        return res