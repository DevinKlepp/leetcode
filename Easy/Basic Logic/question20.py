class Solution:
    def isValid(self, s): # Use stack
        if(len(s) == 0):
            return True
        if(len(s) % 2 == 1):
            return False
        closing = {"}":"{", "]":"[", ")":"("}
        stack = []
        
        for b in s:
            if(b not in closing): # If it is an openning braket
                stack.append(b)
                
            elif(len(stack) != 0 and stack[-1] == closing[b]): # If the top of stack's element is the complement of closing
                stack.pop()
            else:
                return False
        if(len(stack) > 0):
            return False
        return True
