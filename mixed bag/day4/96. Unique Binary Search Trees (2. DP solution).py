class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = dict()
        
        for i in range(n - 1, -1, -1):
            l = i
            r = n - 1
            d = r - l + 1     
                    
            if l == r:
                dp[d] = 1
            elif l == r - 1:
                dp[d] = 2
            else:
                count = 2 * dp[d - 1]
                #count += dp[d - 1] # l as root
                #count += dp[d - 1] # r as root
                for root in range(l + 1, r):       
                    count += dp[root - l] * dp[r - root]                    
                dp[d] = count
                
            #print(dp)

        return dp[n]
