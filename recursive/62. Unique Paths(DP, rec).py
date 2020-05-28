# try 1. without memo: TLE
# try 2. with memo: become DP -> runtime: O(N^2), space:O(N^2)
# try 3. recusive: draw graph get result.


class Solution:
            
    def uniquePaths_DP(self, m: int, n: int) -> int:
                                                                                
        memo = []
        for i in range(0, m + 1):
            memo.append([0] * (n + 1))
                    
        for i in range(m - 1, -1, -1):
            
            for j in range(n - 1, -1, -1):
            
                if i == m - 1 and j == n - 1:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i + 1][j] + memo[i][j + 1]
            
                                        
        return memo[0][0]
    
    def uniquePaths(self, m: int, n: int) -> int:
                                                                                
        def rec(i, j, memo):            
            
            m = len(memo)
            n = len(memo[0])
            
            if (i >= m) or (j >= n):
                return 0
            
            if memo[i][j]:
                return memo[i][j]
            
            if i == m - 1 and j == n - 1:
                memo[i][j] = 1                
                return 1
            
            else:                
                fromDown = rec(i + 1, j, memo)
                fromRight = rec(i, j + 1, memo)
                memo[i][j] = fromDown + fromRight
                return memo[i][j]
                            
        
        memo = []
        for i in range(0, m):
            memo.append([None] * n)
                
        return rec(0, 0, memo)
