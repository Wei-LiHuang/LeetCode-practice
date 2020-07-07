class Solution:
    
    def minDistance(self, w1: str, w2: str) -> int:
        
        '''
        dp[i][j] = min number of operations to make str start from w1[i] equals to str starting from w2[j]        
        dp[i][j]:        
            if w1[i] == w2[j]: dp[i][j] = min(dp[i + 1][j + 1], 1 + dp[i][j + 1], 1 + dp[i + 1][j])
            else: dp[i][j] = 1 + min(insert: dp[i][j + 1], remove: dp[i + 1][j], replace: dp[i + 1][j + 1])                                                             
        '''
        
        m, n = len(w1), len(w2)
        dp = []
        for i in range(0, m + 1):
            dp.append([float('inf')] * (n + 1))        
        
        dp[m][n] = 0
        
        # w2 is "": remove all from w1[i] ... w1[m - 1]
        for i in range(0, m):
            dp[i][n] = m - 1 - i + 1
        
        # w1 is "": insert all from w2[j] ... w2[n - 1]
        for j in range(0, n):
            dp[m][j] = n - 1 - j + 1
                
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if w1[i] == w2[j]:
                    dp[i][j] = min(dp[i + 1][j + 1], 1 + dp[i][j + 1], 1 + dp[i + 1][j])
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
                    
        return dp[0][0]
