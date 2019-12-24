class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        copy = nums
        copy.sort()
        #self.ms(copy)
        print(nums)
        result = copy[0] + copy[1] + copy[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = copy[i] + copy[l] + copy[r]
                if temp == target:
                    return temp
                if abs(temp - target) < abs(result - target):
                    result = temp
                if temp < target:
                    l += 1
                else:
                    r -= 1
        return result
        
        
        
    """    
    def ms(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            l = arr[:mid]
            r = arr[mid:]
        
            self.ms(l)
            self.ms(r)
        
            i = j = k = 0
        
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i+=1
                else:
                    arr[k] = r[j]
                    j+=1
                k+=1
            while i < len(l):
                arr[k] = l[i]
                i+=1
                k+=1
            while j < len(r):
                arr[k] = r[j]
                j+=1
                k+=1
        """
