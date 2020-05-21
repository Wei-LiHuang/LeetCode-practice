class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        left, n = 0, len(nums)        
        for right in range(1, n):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left + 1
            
        
        
        
