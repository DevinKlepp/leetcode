# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/validate-binary-search-tree/solution/

class Solution:
    def isValidBST(self, root):
        return self.check(root, float("-inf"), float("inf"))
    
    def check(self, root, left, right):
        if not root:
            return True
        if not left < root.val < right:
            return False
        
        return self.check(root.left, left, root.val) and self.check(root.right, root.val, right)
        
        
