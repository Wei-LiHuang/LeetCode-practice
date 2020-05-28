class Solution:
    
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        dp = []
        for i in range(0, len(s)):
            dp.append([False] * len(s))
            
        for i in range(len(s) - 1, -1, -1):
            
            for j in range(len(s) - 1, i - 1, -1):
                
                if s[i] != s[j]:
                    continue
                else:
                    if i == j or i + 1 == j:
                        dp[i][j] = True
                        res += 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
            
        
        return res
            
        
