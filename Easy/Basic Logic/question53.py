class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            found = False
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
            if not found:
                digits.insert(0, 1)
                
        return digits
