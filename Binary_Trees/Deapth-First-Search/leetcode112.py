'''
    Leet code 112 - Path Sum 1
'''
class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(node, curSum):
            if not node:
                return False 
            curSum += node.val 
            if not node.left and not node.right:
                return curSum == targetSum
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        return dfs(root, 0)