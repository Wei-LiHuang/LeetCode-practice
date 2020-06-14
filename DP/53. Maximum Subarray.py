class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [float('-inf')] * n
        res = float('-inf')
        for r in range(n - 1, -1, -1):            
            if r == n - 1:
                dp[r] = nums[r]                
            else:
                dp[r] = max(nums[r], nums[r] + dp[r + 1])
            res = max(res, dp[r])
        
        return res
            
