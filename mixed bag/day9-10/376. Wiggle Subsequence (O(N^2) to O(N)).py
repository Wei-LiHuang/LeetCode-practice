# try 1: use two array to record i-th element as start max res -> O(N ^ 2)
# how to reach O(N)? fix the loop within dp loop:
# dp[-][i] = max(1, dp[0][i + 1]), and if a[i] > a[i + 1]: dp[-][i] = max(dp[-][i], 1 + dp[+][i + 1])


class Solution:
    
    def wiggleMaxLength(self, a: List[int]) -> int:
        
        n = len(a)
        if n == 0:
            return 0
        
        
        dp = []
        dp.append([-float('inf')] * n) # -
        dp.append([-float('inf')] * n) # +
        
        
        for i in range(n - 1, -1, -1):
            
            # -:
            if i == n - 1:
                dp[0][i] = 1
            else:
                #dp[0][i] = 1
                #for j in range(i, n):
                    #if a[j] < a[i]:
                        #dp[0][i] = max(dp[0][i], 1 + dp[1][j])                                
                dp[0][i] = max(dp[0][i + 1], 1)
                if a[i] > a[i + 1]:                    
                    dp[0][i] = max(dp[0][i], 1 + dp[1][i + 1])
                
                        
            # +:
            if i == n - 1:
                dp[1][i] = 1
            else:
                #dp[1][i] = 1
                #for j in range(i, n):
                    #if a[j] > a[i]:
                        #dp[1][i] = max(dp[1][i], 1 + dp[0][j])
                dp[1][i] = max(dp[1][i + 1], 1)
                if a[i] < a[i + 1]:  
                    dp[1][i] = max(dp[1][i], 1 + dp[0][i + 1])
                                                              
                        
        
        return max(dp[0][0], dp[1][0])
