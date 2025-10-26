class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right

# Recursive solution
def insertIntoBST(root,val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)
    else:
        root.left = self.insertIntoBST(root.left, val)
    return root
    
# Iterative Solution        
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    curr = root 
    while True:
        if val > curr.val:
            if not curr.right:
                curr.right = TreeNode(val)
                return root
            curr = curr.right 
        else:
            if not curr.left:
                curr.left = TreeNode(val)
                return root 
            curr = curr.left
    