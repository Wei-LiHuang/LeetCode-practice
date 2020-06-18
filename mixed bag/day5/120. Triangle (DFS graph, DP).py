# 1. dfs -> graph, need memo, but it said only O(n = number of row = last row length) space -> matbe not
# 2. DP

class Solution:
    
    def minimumTotal(self, tri: List[List[int]]) -> int:
        
        m = len(tri)
        dp = tri[m - 1]
        
        for r in range(m - 2, -1, -1):            
            for c in range(0, r + 1):
                dp[c] = tri[r][c] + min(dp[c], dp[c + 1])                                                
        
        return dp[0]
        
