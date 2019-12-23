class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        stack = []
        total = 0
        i = 0
        while i < len(height):
            # If stack is empty or current height < top of stack
            if not stack or height[i] <= height[stack[len(stack) - 1]]:
                # Add current height to stack and increment i
                stack.append(i)
                i+=1
                    
            else: # If current height > top stack val
                popped = stack.pop(len(stack) - 1)
                if len(stack) > 0: # If stack not empty
                    minHeight = min(height[stack[len(stack) - 1]], height[i])
                    total += (minHeight - height[popped]) * (i - stack[len(stack) - 1] - 1) 
        return total
