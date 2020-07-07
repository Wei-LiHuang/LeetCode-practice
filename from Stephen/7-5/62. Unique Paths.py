class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        '''        
        dp[m - 1][n - 1] = dp[m - 1][n - 2] + dp[m - 2][n - 1]        
        ...        
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]                        
        ...        
        dp[0][0] = 1                
        '''                
        dp = []
        for i in range(0, m):
            dp.append([0] * n)
            
        for i in range(0, m):
            for j in range(0, n):
                
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        return dp[m - 1][n - 1]
                
