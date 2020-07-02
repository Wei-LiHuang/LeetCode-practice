"""
# the base is correct
if p[i][0] == s[j] or p[i][0] == '.': 
    dp[i][j] = (dp[i + 1][j] # * = 0 pair                            
            or dp[i][j + 1] # * = 1 pair, keep using <- this one
            or dp[i + 1][j + 1]) # * = 1 pair
"""

class Solution:
    def isMatch(self, S: str, P: str) -> bool:
        
        # setup:
        N, M = len(S), len(P)        
        s = []
        for j in range(0, N):
            s.append(S[j])        
        p = []
        for i in range(0, M):
            if P[i] == '*':
                continue            
            if i == M - 1:                
                p.append(P[i])
            else:
                if P[i + 1] == "*":
                    p.append(P[i : i + 2])
                else:
                    p.append(P[i])
        
        
        n, m = len(s), len(p) 
        # DP arr:
        dp = []
        for i in range(0, m + 1):
            dp.append([None] * (n + 1))
        
        # s, p are both empty
        dp[m][n] = True
        
        # s is empty, p = [pi, pi + 1, ..., pm - 1]
        # if the elements left are all _*, then true
        # else: false
        for i in range(m - 1, -1, -1):
            if i == m - 1:
                if len(p[i]) == 2:
                    dp[i][n] = True
                else:
                    dp[i][n] = False            
            else:
                dp[i][n] = (len(p[i]) == 2 and dp[i + 1][n])
    
        # p is empty, s = [sj, sj + 1, ..., sn - 1], no match, all false
        for j in range(0, n):
            dp[m][j] = False
                                        
        # calculate dp:
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                # has *
                if len(p[i]) == 2:
                    # the base is correct
                    if p[i][0] == s[j] or p[i][0] == '.': 
                        dp[i][j] = (dp[i + 1][j] # * = 0 pair                            
                                or dp[i][j + 1] # * = 1 pair, keep using
                                or dp[i + 1][j + 1]) # * = 1 pair
                    else:
                        # the base is wrong, _* can only use as 0 pair:
                        dp[i][j] = dp[i + 1][j]                                        
                else:
                    # the base is correct
                    if p[i] == s[j] or p[i] == '.':
                        dp[i][j] = dp[i + 1][j + 1]
                    else:
                        # the base is wrong
                        dp[i][j] = False
        
        
        return dp[0][0]