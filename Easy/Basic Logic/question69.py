class Solution: # Binary search
    def mySqrt(self, x: int) -> int: 
        if(x < 2):
            return x
        low = 1
        high = x
        while(low <= high):
            mid = low + (high - low) // 2
            if(mid == x/mid):
                return mid
            elif(mid < x / mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
