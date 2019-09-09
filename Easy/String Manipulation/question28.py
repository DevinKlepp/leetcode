class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or needle == haystack:
            return 0
        elif len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if len(needle) <= len(haystack[i:]): # If length of needle is less than what is left
                if haystack[i : i + len(needle)] == needle:
                    return i
        return -1
