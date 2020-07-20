class Solution:
    
    def minCut(self, s: str) -> int:        
        def isPal(s):
            n, dp = len(s), []
            for i in range(0, n):
                dp.append([False] * n)
            for i in range(n - 1, -1, -1):
                for j in range(n - 1, i - 1, -1):
                    if i == j:
                        dp[i][j] = True
                    elif i == j - 1 and s[i] == s[j]:
                        dp[i][j] = True
                    elif s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
            return dp                          
        
        pal = isPal(s) 
        
        '''
        dp[i]: min cut for subStr(i, n - 1) 
        '''
        
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            if pal[i][n - 1]:
                dp[i] = 0
            else:            
                for j in range(i, n):
                    if pal[i][j]:
                        dp[i] = min(dp[i], 1 + dp[j + 1])
        return dp[0]
