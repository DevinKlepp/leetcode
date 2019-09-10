class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for  _ in range(n - 1):
            dig, temp, count = s[0], '', 0
            
            for char in s:
                if dig == char:
                    count += 1
                else:
                    temp += str(count) + dig
                    dig = char
                    count = 1
            temp += str(count) + dig
            s = temp
        return s
