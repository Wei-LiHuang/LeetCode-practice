class Solution:
    
    def minPathSum(self, dp: List[List[int]]):
        
        '''
        dp[i][j] = dp[i][j] + min(dp[i - 1][j], dp[i][j - 1])        
        '''
        m = len(dp)
        n = len(dp[0])
        
        for i in range(0, m):
            for j in range(0, n):
                
                if i == 0 and j == 0:
                    dp[i][j] = dp[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j] + min(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m - 1][n - 1]
