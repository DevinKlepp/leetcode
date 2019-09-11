class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left = 0
        right = x
        while left + 1 < right:
            mid = left + (right - left) // 2
            if x // mid > mid:
                left = mid
            elif x // mid < mid:
                right = mid
            else:
                return mid
        return left
