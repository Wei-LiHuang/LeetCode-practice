# same as 10. Regular Expression Matching, 72. Edit Distance

class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)
        
        dp = []
        for i in range(0, m + 1):
            dp.append([None] * (n + 1))
            
        # s, p are both empty:
        dp[m][n] = True
        
        # s is empty, p = [pj, p j + 1, ..., p n - 1]
        for j in range(n - 1, -1, -1):
            if p[j] == '*':            
                dp[m][j] = dp[m][j + 1]
            else:
                dp[m][j] = False
                
        # p is empty, s = [si, si + 1, ..., s m - 1]
        for i in range(0, m):            
            dp[i][n] = False
            
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                      
                if p[j] == '*':                    
                    dp[i][j] = dp[i + 1][j] or dp[i + 1][j + 1] or dp[i][j + 1]                                        
                elif p[j] == '?':
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = (p[j] == s[i]) and dp[i + 1][j + 1]
                    
        return dp[0][0]
            
        
        
