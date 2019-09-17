# SLICING EXPENSIVE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# L child is 2n+1, r is 2n + 2
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = (len(nums)) // 2
        
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])
        return head
        
#NO SLICING

class Solution:
    def sortedArrayToBST(self, nums):
        return self.build(nums, 0, len(nums)-1)
    
    def build(self, nums, low, high):
        if low == high:
            return TreeNode(nums[low])
        elif low < high:
            mid = (low+high)//2
            node = TreeNode(nums[mid])
            node.left = self.build(nums, low, mid-1)
            node.right = self.build(nums, mid+1, high)
            return node
