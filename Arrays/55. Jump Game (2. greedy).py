#greedy approach:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums) - 1
        
        tgt = n
        
        for i in range(n - 1, -1, -1):            
            if (i + nums[i]) >= tgt:
                tgt = i
        
        return tgt == 0
