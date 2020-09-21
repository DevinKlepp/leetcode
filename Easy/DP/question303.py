class NumArray:
    def __init__(self, nums: List[int]):
        self.ret = [0]
        if(not nums):
            return None
        for i in range(0, len(nums)):
            self.ret.append(nums[i] + self.ret[i])
            
    def sumRange(self, i: int, j: int) -> int:
        return self.ret[j + 1] - self.ret[i]
