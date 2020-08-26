# Understand 
"""
We want to write a function that given a binary tree returns if the tree is balanced.
Balanced here meaning that the deepest level of the left and right branches differ by no more than 1


"""
# Plan
"""


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: TreeNode) -> bool:

    def getHeight(n):
        if n == None:
            return 0
        
        return 1 + (getHeight(n.left), getHeight(n.right))
    

    if root is None:
        return True
    l_height = getHeight(root.left)
    r_height = getHeight(root.right)
    return abs(l_height - r_height) <= 1 and isBalanced(root.left) and isBalanced(root.right)