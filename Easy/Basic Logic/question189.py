class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                nxt = (current + k) % len(nums)
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                current = nxt
                count += 1
                if start == current:
                    break
            
            start += 1
# OR
# k = k % len(nums)
# nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]
