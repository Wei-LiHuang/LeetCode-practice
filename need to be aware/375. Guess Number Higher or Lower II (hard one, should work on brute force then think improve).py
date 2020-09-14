class Solution:    
    def getMoneyAmount(self, n: int) -> int:
        
        
        dp = []
        for i in range(0, n + 1):
            dp.append([float('inf')] * (n + 1))
            
        for i in range(n, 0, -1):
            for j in range(i, n + 1):                
                if i == j:
                    dp[i][j] = 0
                elif i == j - 1:
                    dp[i][j] = i
                elif i == j - 2:
                    dp[i][j] = i + 1
                elif i == j - 3:
                    dp[i][j] = j - 1 + i
                else:                    
                    # mid = (i + j) // 2
                    # for k in range(mid, j): ---> this is from Stefan's solution                    
                    for k in range(i + 1, j): # --> mine version
                        dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))
        
        return dp[1][n]
                    
        
