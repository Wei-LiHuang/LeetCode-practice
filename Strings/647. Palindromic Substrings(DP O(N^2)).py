#dp: run time: O(N^2), space: O(N^2)

class Solution:
    
    def countSubstrings(self, s: str) -> int:
        
        res, n = 0, len(s)
        
        dp = []
        for i in range(0, n):
            dp.append([False] * n)
            
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                
                if i == j:
                    dp[i][j] = True
                    res += 1
                elif s[i] == s[j] and j - 1 == i:
                    dp[i][j] = True
                    res += 1
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res += 1
        
        return res
