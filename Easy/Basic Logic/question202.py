class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n != 1:
            if n in seen:
                return False
            else:
                seen[n] = True
            temp = 0
            while n > 0:
                temp += (n % 10)**2
                n //= 10
            n = temp
            
        return True
