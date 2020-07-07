class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        
        '''
        dp[i][j]: LCS(a[i] ~ a[m - 1], b[j] ~ b[n - 1])
        if a[i] == b[j]:
            dp[i][j] = max(1 + dp[i + 1][j + 1], dp[i][j + 1], dp[i + 1][j])
        if a[i] != b[j]:
            dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])                        
        '''
        m, n = len(a), len(b)
        dp = []
        for i in range(0, m + 1):
            dp.append([0] * (n + 1))
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):                
                if a[i] == b[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]                    
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j + 1])                        
        #print(dp)
        return dp[0][0]
