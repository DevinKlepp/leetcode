# n time and space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ht = {}
        for i in range(len(nums)):
            if nums[i] not in ht:
                ht[nums[i]] = i
            else:
                del ht[nums[i]]
        for element in ht:
            return element

        # n time 1 space   
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
