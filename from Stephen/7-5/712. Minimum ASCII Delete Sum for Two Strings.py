class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        
        '''        
        dp[i][j]: min ASCII Delete sum to make str from a[i] and str from b[i] he same
        
        dp[m][n]: both are empty -> 0
        dp[i][n]: b is empty, need to delete all a[i] ~ a[m - 1]
        dp[m][j]: a is empty, need to delete all b[j] ~ b[n - 1]
        
        dp[i][j]:
            if a[i] == a[j]:
                dp[i][j] = min(dp[i + 1][j + 1], ac[i] + dp[i + 1][j], bc[j] + dp[i][j + 1])
            else:
                dp[i][j] = min(ac[i] + dp[i + 1][j], bc[j] + dp[i][j + 1], ac[i] + bc[j] + dp[i + 1][j + 1])                
        '''
        
        m, n, dp = len(a), len(b), []
        
        for i in range(0, m + 1):
            dp.append([0] * (n + 1))
        
        dp[m][n] = 0
        
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(a[i])
            
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(b[j])
            
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = min(dp[i + 1][j + 1], ord(a[i]) + dp[i + 1][j], ord(b[j]) + dp[i][j + 1])
                else:
                    dp[i][j] = min(ord(a[i]) + dp[i + 1][j], ord(b[j]) + dp[i][j + 1], ord(a[i]) + ord(b[j]) + dp[i + 1][j + 1]) 
                
        return dp[0][0]
