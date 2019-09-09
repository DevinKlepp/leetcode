class Solution: # In place algorithm, swapping the new end
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        for i in range(1, len(nums)):
            if(nums[current] != nums[i]):
                current += 1
                nums[current] = nums[i]
        return current + 1
