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
    
    class Solution:
    def rec(self, n, ht): # Memoized
        if(n == 1):
            return 1
        elif(n == 2):
            return 2
        elif(n in ht):
            return ht[n]

        ht[n] = self.rec(n - 1, ht) + self.rec(n - 2, ht)
        return ht[n]
    
    def climbStairs(self, n: int) -> int:
        ht = {}
        return self.rec(n, ht)
    
    def climbStairs(self, n: int) -> int: # DP Way
        if(n < 4):
            return n
        ht = {}
        ht[1] = 1
        ht[2] = 2
        for i in range(3, n + 1):
            ht[i] = ht[i - 1] + ht[i - 2]
        return ht[n]
        
