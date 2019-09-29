class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result
        # return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5) # Equiv. to diviging by 25 in second itteration
        
