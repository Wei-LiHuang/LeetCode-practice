class Solution:
    
    def numRollsToTarget(self, d: int, f: int, tgt: int) -> int:
        
        '''
        dp[m, tgt] = dp[m - 1, tgt - 0] + dp[m - 1, tgt - 1] + ... + dp[m - 1, tgt - f]
                            
        dp[i, j]:
             = 0, if j > (i * fn-1)
             = sum(dp[i - 1, j - k]), k = 1 ~ f
        '''
        
        m = d + 1
        dp = []
        for i in range(0, m):
            dp.append([0] * (tgt + 1))
        
        dp[0][0] = 1        
        for i in range(0, m):
            for j in range(1, tgt + 1):                
                if j > (i) * f:
                    break
                else:
                    if i == 1 and j <= f:                        
                        dp[i][j] = 1                    
                    else:
                        for k in range(1, f + 1):
                            if j - k >= 0:
                                dp[i][j] += dp[i - 1][j - k]
                                
                                                                                      
        return dp[m - 1][tgt] % (10 ** 9 + 7)
