class Solution:
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)
        dp = []
        for i in range(0, m + 1):
            dp.append([0] * (n + 1))
                          
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

                        
        return dp[0][0]
