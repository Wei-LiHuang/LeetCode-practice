class Solution:
    def strangePrinter(self, s: str) -> int:
        
        n = len(s)
        if n == 0:
            return 0
        
        dp = []
        for i in range(0, n):
            dp.append([float('inf')] * n)
            
        for i in range(n - 1, -1, -1):
            for j in range(i, n):                
                if i == j:
                    dp[i][j] = 1                
                else:
                    if s[i] == s[j]:
                        dp[i][j] = min(1 + dp[i + 1][j - 1], dp[i][j - 1])
                    else:
                        #mine:
                        #dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
                        
                        #ans:
                        for k in range(i, j):                            
                            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                    
        #print(dp)                    
        return dp[0][n - 1]       
