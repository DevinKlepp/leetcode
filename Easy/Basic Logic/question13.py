class Solution(object):
    def romanToInt(self, s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        num = 0
        prev = None
        for char in reversed(s):
            if(prev == None or d[char] >= d[prev]):
                num += d[char]
                prev = char
            elif(d[char] < d[prev]):
                num -= d[char]
                prev = char
        return num
