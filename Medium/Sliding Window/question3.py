class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) < 2):
            return len(s)
        used = {}
        maxval = 1
        l = used[s[0]] = 0
        for r in range(1, len(s)):
            if(s[r] in used and l <= used[s[r]]): # If variable is used AND start is less than
                l = used[s[r]] + 1                # the location of the previous time this has been encountered,
            else:                                 # because if it wasn't, it isn't repeating
                maxval = max(r - l + 1, maxval)
            used[s[r]] = r
        return maxval
        
