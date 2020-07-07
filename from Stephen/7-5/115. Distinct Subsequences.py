# first come up with O(^3) sol, then made it O(N^2)

class Solution:
    
    def numDistinct(self, s: str, t: str) -> int:
        
        '''
        dp[i][j]: number of str start from s[i] can represent the str start from t[j]
        
        if a[i] == b[j]:
            dp[i][j] = dp[i + 1][j + 1] + dp[i][j + 1]                                    
        else:
            dp[i][j] = 0 + dp[i][j + 1]                                
        '''
        
        m, n = len(s), len(t)
        
        dp = []
        for i in range(0, m + 1):
            dp.append([0] * (n + 1))
            
        dp[m][n] = 1
        
        for i in range(0, m):
            dp[i][n] = 1
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):                
                #c1, c2 = s[i], t[j]        
                dp[i][j] = dp[i + 1][j]
                
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                    #for k in range(i + 1, m + 1):                            
                        #dp[i][j] += dp[k][j + 1]
        
        return dp[0][0]
        #print(dp)
        
        #res = 0
        #for i in range(0, m):
            #res += dp[i][0]
        
        #return res
        
        
