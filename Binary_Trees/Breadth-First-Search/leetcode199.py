'''
    leetcode 199 - binary tree right side view
    Given the root of a binary tree, imagine yourself standing on the right side of it, 
    return the values of the nodes you can see ordered from top to bottom.
'''
import collections
class Solution:
    def rightSideView(self, root):
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None 
            qlen = len(q)
            
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:        
                res.append(rightSide.val)