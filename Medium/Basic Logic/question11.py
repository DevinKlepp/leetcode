class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxval = 0
        i, j = 0, len(height) - 1
        while i < j: # While left < right
            maxval = max(maxval, min(height[i], height[j]) * (j - i))
            if(height[j] > height[i]):
                i += 1
            else:
                j -= 1
        return maxval
