# 1 4 5
# 2 7 6
# 6 8 7

class Solution:
    
    def minPathSum(self, dp: List[List[int]]) -> int:
        
        m = len(dp)
        n = len(dp[0])
                       
        for r in range(0, m):            
            for c in range(0, n):                
                if r == 0 and c == 0:                    
                    continue                
                fromTop, fromLeft = float('inf'), float('inf')
                if r != 0:
                    fromTop = dp[r - 1][c]                
                if c != 0:                                
                    fromLeft = dp[r][c - 1]
                    
                dp[r][c] += min(fromLeft, fromTop)
                
        
        
        return dp[m - 1][n - 1]
        
