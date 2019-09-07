class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ht = {} # Last location for each character
        longest = i = 0
        
        for j, c in enumerate(s): # sliding window of [i, j] 
            if c in ht and i <= ht[c]: # If matching char has been found AND start is less than the location of the 
                                             # prev time this char has been encountered, because if it wasn't, it isn't repeating
                i = ht[c] + 1 # Moving window to start at the next char beside the repeted character
            
            else:
                longest = max(j - i + 1, longest)
            ht[c] = j
        return longest
