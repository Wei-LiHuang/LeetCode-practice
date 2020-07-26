class Solution:
    
    def stoneGameII(self, a: List[int]) -> int:
        
        '''
            Alex max point = picked + points after lee's min pick
            lee min pick = picked' + points after alex's min pick ...
            
            dp[i][m]: start i-th element, M = m, max point a player can get            
            
            if i + 2 * m >= n:
                can get all -> dp[i][m] = sum(a[i:n])            
            else:                
                dp[i][m] = max(dp[i][m], 
                                        sum(a[i : i + x]) - dp[i + x][max(M, x)] ... this is wrong
                                        sum(a[i : n]) - dp[i + x][max(M, x)] ... correct                        
                            )
                         = max(dp[i][m], sum(a[i:n]) - min(dp[i + x][max(M, x)], for x in range(1, 2 * m)))
        '''
        n = len(a)
        dp = []
        for i in range(0, n):
            dp.append([-float('inf')] * (n + 1))
        
        for i in range(n - 1, -1, -1):
            for m in range(n, 0, -1):                
                if i + 2 * m >= n:
                    dp[i][m] = sum(a[i:n])                                    
                else:
                    minX = -1
                    minNextRoundPoint = float('inf')
                    maxDis = min((n - 1) - i + 1, 2 * m + 1)
                    # find the min next round point by scanning all possible x:
                    for x in range(1, maxDis):                                      
                        if minNextRoundPoint > dp[i + x][max(x, m)]:
                            minX = x
                            minNextRoundPoint = dp[i + x][max(x, m)]
                
                    dp[i][m] = max(dp[i][m], sum(a[i:n]) - minNextRoundPoint)
                        
        return dp[0][1]
