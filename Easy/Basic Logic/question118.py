class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        returned = [None] * numRows 
        returned[0] = [1]
        for i in range(1, numRows):
            returned[i] = [None] * (i + 1)
            returned[i][0], returned[i][-1]  = 1, 1
            j = 0
            while j + 1 < len(returned[i - 1]):
                returned[i][j + 1] = returned[i - 1][j] + returned[i - 1][j + 1]
                j += 1
        return returned
