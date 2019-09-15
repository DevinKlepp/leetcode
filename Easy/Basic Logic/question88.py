class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0: # Reaches this if the first int in nums1 is larger than the rest in nums2
            nums1[:n] = nums2[:n] # take the rest from nums2 and put them on the front
