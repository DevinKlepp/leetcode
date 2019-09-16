# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, l, r) -> bool:
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        return (l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left))
