class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempmax = -2**31
        ret = -2**31
        for i in range(0, len(nums)):
            tempmax = max(tempmax + nums[i], nums[i])
            if(tempmax > ret):
                ret = tempmax
        return ret
            
