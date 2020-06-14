# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# only know the math solution can pass this

class Solution:
    
    def nextPermutation(self, nums: List[int]) -> None:
        
        def reverse(a, l, r):
            while l < r:
                temp = a[l]
                a[l] = a[r]
                a[r] = temp
                l += 1
                r -= 1
            return
        
        found = False
        n = len(nums)
        
        K = -1
        for k in range(n - 2, -1, -1):            
            if nums[k] < nums[k + 1]:
                K = k
                found = True
                break
        
        if found == False:
            reverse(nums, 0, n - 1)
            return
        
        I = -1
        for i in range(K + 1, n):            
            if nums[i] > nums[K]:
                I = i
            
        temp = nums[I]
        nums[I] = nums[K]
        nums[K] = temp
        
        reverse(nums, K + 1, n - 1)
        
        return
        
        
