class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        '''
        cost = [c0, c1, c2, ... , cn-1]
        find th minimum cost to reach stair n
        dp[n] = min( c(n - 1) + dp[n - 1], c(n - 2) + dp[n - 2] )
        '''
        
        n = len(cost)
        inf = float('inf')
        dp = [inf] * (n + 1)        
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
            
        return dp[n]
