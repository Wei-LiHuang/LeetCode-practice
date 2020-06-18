class Solution:
    
    def minCut(self, s: str) -> int:                
                
        def getRes(s, cur, minCut, dp):
            
            if cur in minCut:
                return minCut[cur]
            
            n = len(s)
            
            if cur == n - 1:
                minCut[cur] = 1
                return minCut[cur]
            
            cut = float('inf')
            for i in range(n - 1, cur - 1, -1):               
                if dp[cur][i]:
                    # s[cur] ~ s[i] is palindrome
                    # cut = {s(cur) ~ s[i]}, {s[i + 1] ~ s[n - 1]}                    
                    nextCut = 1 + minCut[i + 1]
                    cut = min(cut, nextCut)
                    
            minCut[cur] = cut            
            return
            
                                                                                    
        n, dp = len(s), []
        if n == 0:
            return 0
        for i in range(0, n):
            dp.append([False] * n)
            
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1 and s[i] == s[j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
        
        minCut = dict()
        minCut[n] = 0
        
        for cur in range(n - 1, -1, -1):
            getRes(s, cur, minCut, dp)
            
        return minCut[0] - 1

        
