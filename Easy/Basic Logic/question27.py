class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # i and j traverse at most n steps
        n = len(nums)
        while(i < n):
            if(nums[i] == val):
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        3return i
        #int i = 0; # at most 2n steps
        #int n = nums.length;
        #while (i < n) {
        #    if (nums[i] == val) {
        #        nums[i] = nums[n - 1];
        #        // reduce array size by one
        #        n--;
        #    } else {
        #        i++;
        #    }
        #}
        #return n;