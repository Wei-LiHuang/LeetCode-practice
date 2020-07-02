class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        m, n = len(w1), len(w2)
        
        dp = []
        for i in range(0, m + 1):
            dp.append([float('inf')] * (n + 1))
            
        # w1, w2 empty:
        dp[m][n] = 0
                    
        # w2 empty: min op number = del the rest of w1:
        # w1 = [ci, ci + 1, ... , cm - 1]  -> del from w1, ops = (m - 1 - i + 1)
        # w2 = [empty]
        for i in range(0, m):
            dp[i][n] = m - i
            
        # w1 empty: min op number = insert the rest of w2 into w1:
        # w1 = [empty]
        # w2 = [sj, sj + 1, ... , sn - 1], n - 1 - j + 1 = n - j
        for j in range(0, n):
            dp[m][j] = n - j
            
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):                
                if w1[i] == w2[j]:
                    # no edit
                    dp[i][j] = min(dp[i][j], dp[i + 1][j + 1])

                
                # insert into w1:
                dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])
                
                # replace w1[i] with w2[j]:
                dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j + 1])
                
                # del w1[i]:
                dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
                
                #dp[i][j] = min([dp[i][j], 1 + dp[i][j + 1], 1 + dp[i + 1][j + 1], 1 + dp[i + 1][j]])
                
            #print(dp)
                
        
        return dp[0][0]
