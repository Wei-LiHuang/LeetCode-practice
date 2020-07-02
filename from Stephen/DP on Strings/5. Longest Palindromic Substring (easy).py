# s[i] to s[j] is a palindrome if s[i] == s[j] and s[i + 1], s[j - 1] is also a palindrome
# maintain a 2-D array: dp[i][j] = true, if s[i] ~ s[j] is P, else: dp[i][j] = false
# also the size of the dp array is (n + 1) * (n + 1) or n * n? -> n * n

# dp approach:
#    b  a   b   a    d
# b  t  ba  bab baba babad
# a  x  t   ab  aba  abad
# b  x  x   t   ba   bad
# a  x  x   x   t    ad
# d  x  x   x   x    t
#
#  x = false (i > j)

# dp[i = n - 1][j = n - 1] = true ...(when i == j)

# dp[i = n - 2][j = n - 1] = (s[i] == s[j]) ... (when j - i == 1)
# dp[i = n - 2][j = n - 2] = true ... (when i == j)

# dp[i = n - 3][j = n - 1] = (s[i] == s[j]) and (dp[n - 2][n - 2] = d[i + 1][j - 1])...when j - i >= 2
# dp[i = n - 3][j = n - 2] = (s[i] == s[j]) ... (when j - i == 1)
# dp[i = n - 3][j = n - 3] = true ... (when j == i)

# dp[i = n - 4][j = n - 1] = (s[i] == s[j]) and (dp[n - 3][n - 2] = d[i + 1][j - 1])...when j - i >= 2
# ... and when finished the dp table, we got all the subsequence is palindrome or not.
# space: O(N ^ 2), runtime: i: from (n - 1) to 0, j from (n - 1) to i -> 1 + 2 + 3 + ... + n => O(n^2)

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        
        n, dp = len(s), []
        for i in range(0, n):
            dp.append([False] * n)
            
            
        l = -float('inf')    
        res = ""
        for i in range(n - 1, -1, -1):
            
            for j in range(n - 1, i - 1, -1):
                
                if i == j:
                    dp[i][j] = True
                    
                elif i == j - 1:
                    dp[i][j] = (s[i] == s[j])
                
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                    
                if dp[i][j] and (j - i + 1) > l:
                    l = (j - i + 1)
                    res = s[i:j + 1]
            
            
        return res
