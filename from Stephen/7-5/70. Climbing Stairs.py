class Solution:
    
    def climbStairs(self, n: int) -> int:
        '''
        n steps, can take 1 or 2 step
        
        dp[n] = dp[n - 1] + dp[n - 2]
        
        ...
        
        dp[i] = dp[i - 1] + dp[i - 2]
        
        ...
        
        dp[2] = 1 + 1
        
        ...
        
        dp[1] = 1
        dp[0] = 1
        
        '''
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n]
