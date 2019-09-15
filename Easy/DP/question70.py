class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        nums = [None] * (n + 1) # Need space for the 0 spot
        nums[0] = 1
        nums[1] = 1
        for i in range(2, n + 1): # Want to run it through the n index
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n]
        
# General diff numbers

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        nums = [None] * (n + 1)
        nums[0] = 1
        for i in range(1, n + 1):
            total = 0
            for j in [1, 2]:
                if i - j >= 0:
                    total += nums[i - j]
            nums[i] = total
        return nums[n]
