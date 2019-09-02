class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        ht = {}
    
        for i in range(0,len(nums)):
            if target - nums[i] not in ht: # If complement isn't in table yet, add the original
                ht[nums[i]] = i 
            else: # If complement is found, return the index of the original and the current index (complement)
                return [ht[target - nums[i]], i]
