class Solution(object):
    def reverse(self, x):
        sign = False
        if(x < 0): 
            sign = True
            x = abs(x)
        count = 1
        new = 0
        while(x != 0):
            temp = x % 10
            new = new * 10 + temp
            x = x / 10
        if(new < - 2 ** 31 or new > 2 ** 31 - 1):
            return 0
        if(sign): 
            new = new * -1
        return new 
