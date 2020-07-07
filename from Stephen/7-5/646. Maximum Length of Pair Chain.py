class Solution:
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        def cmp(p1, p2):
            if p1[1] == p2[1]:
                return p1[0] - p2[0]            
            else:
                return p1[1] - p2[1]
            
        
        if len(pairs) == 0:
            return 0
        
        pairs = sorted(pairs, key = cmp_to_key(cmp))
        
        #print(pairs)
        
        '''
        dp[n - 1] = 1
        dp[n - 2] = 1, if p[n - 2][1] >= p[n - 1][0]
                  = 1 + dp[n - 1], if p[n - 2][1] < p[n - 1][0]
        ...
        
        dp[i] = 1 + dp[k], where pairs[k][0] > pairs[i][1], k <= n - 1
        
        -> O(N ^ 2)  runtime
        '''
        n = len(pairs)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if pairs[j][0] > pairs[i][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    break
                                    
        return dp[0]
