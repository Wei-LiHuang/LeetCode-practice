#try 1: DP -> pass
#try 2: recursive without memo: TLE
#try 3: recursive with memo: pass, slow

class Solution:
    
    def uniquePathsWithObstaclesDP(self, b: List[List[int]]) -> int:
        
        m = len(b)
        
        if m == 0:
            return 0
        
        n = len(b[0])
                
        dp = []
        for i in range(0, m + 1):
            dp.append([0] * (n + 1))
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if b[i][j] == 1:
                    dp[i][j] = 0                
                else:
                    if i == m - 1 and j == n - 1:
                        dp[i][j] = 1
                    else:                        
                        dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]
    
    
    def uniquePathsWithObstaclesWithoutMemo(self, b: List[List[int]]) -> int:
        
        def rec(r: int, c: int, b: List[List[int]]):
            
            m, n = len(b), len(b[0])
            
            if b[r][c] != 1 and r == m - 1 and c == n - 1:
                return 1
            else:
                if b[r][c] == 1:
                    return 0
                else:                                    
                    fromDown, fromRight = 0, 0
                    if r < m - 1:                        
                        fromDown = rec(r + 1, c, b)
                    
                    if c < n - 1:                        
                        fromRight = rec(r, c + 1, b)
                    
                    return fromDown + fromRight
        
                
        return rec(0, 0, b)   
            
        
    def uniquePathsWithObstacles(self, b: List[List[int]]) -> int:
        
        def rec(r: int, c: int, b: List[List[int]], memo: List[List[int]]):
            
            m, n = len(b), len(b[0])
            
            if memo[r][c]:
                return memo[r][c]
            
            if b[r][c] != 1 and r == m - 1 and c == n - 1:
                memo[r][c] = 1
                return 1
            else:
                if b[r][c] == 1:
                    memo[r][c] = 0
                    return 0
                else:                                    
                    fromDown, fromRight = 0, 0
                    if r < m - 1:                        
                        fromDown = rec(r + 1, c, b, memo)
                    
                    if c < n - 1:                        
                        fromRight = rec(r, c + 1, b, memo)
                    
                    memo[r][c] = fromDown + fromRight
                    return memo[r][c]
        
        
        m = len(b)        
        if m == 0:
            return 0
        
        n = len(b[0])                
        memo = []
        for i in range(0, m):
            memo.append([None] * (n))        
                
        return rec(0, 0, b, memo)       
