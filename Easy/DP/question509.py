class Solution:
    def fib(self, N: int) -> int:
        nums = [0, 1]
        for i in range(2, N + 1):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[N]