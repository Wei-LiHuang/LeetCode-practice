class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        '''
        dp[i, j]: is subStr[i : j + 1] a palindrome
        if True: update max Length and res string            
        '''                
        n, dp = len(s), []
        
        for i in range(0, n):
            dp.append([False] * n)
            
        res, maxL = "", 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):                
                
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    if s[i] == s[j]:
                        dp[i][j] = True                           
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                    
                if dp[i][j] and j - i + 1 > maxL:
                    maxL = j - i + 1
                    res = s[i : j + 1]
                    
        return res
