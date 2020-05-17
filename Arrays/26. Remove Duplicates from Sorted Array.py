class Solution(object):
    def removeDuplicates(self, nums):
        curP = 0
        for i in range(1, len(nums)):            
            if nums[i] != nums[curP]:             
                curP += 1
                nums[curP] = nums[i]
        return curP + 1
        
