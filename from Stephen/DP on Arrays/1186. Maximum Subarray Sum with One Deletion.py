class Solution:
    def maximumSum(self, a: List[int]) -> int:
        
        n = len(a)
        if n == 0:
            return 0
        
        #dp = [-float('inf')] * n          
        res = -float('inf')        
        noSkip = -float('inf')
        skip = -float('inf')
        
        for i in range(n - 1, -1, -1):                        
            if i == n - 1:                
                #dp[i] = a[i]                                
                noSkip = a[i]
                
            elif i ==  n - 2:
                
                temp = noSkip
                #dp[i] = max(a[i], a[i] + dp[i + 1])
                noSkip = max(a[i], a[i] + noSkip)
                #skip = dp[i + 1]
                skip = temp
                
            else:
                temp = noSkip
                #dp[i] = max(a[i], a[i] + dp[i + 1])
                noSkip = max(a[i], a[i] + noSkip)
                
                #skip = max(a[i] + skip, dp[i + 1])
                skip = max(a[i] + skip, temp)
                
            #res = max([res, dp[i], skip])
            res = max([res, noSkip, skip])

        return res
