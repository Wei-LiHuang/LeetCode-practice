# runtime: O(N^2), sapce: O(N)

class Solution:
    
    def findNumberOfLIS(self, a: List[int]) -> int:
        
        n = len(a)        
        if n == 0:
            return 0
        
        maxL = -float('inf')        
        dp = []
        
        for i in range(0, n):
            dp.append([-float('inf'), 0])
            
        count = dict()        
        for i in range(n - 1, -1, -1):                    
            if i == n - 1:
                dp[i] = [1, 1]
                maxL = 1
                count[1] = 1
                continue
            else:                            
                dp[i][0] = 1
                dp[i][1] = 1
                
                for j in range(i + 1, n):
                    
                    if a[j] > a[i]:                        
                        newL = 1 + dp[j][0]                                                                        
                        if newL > dp[i][0]:
                            dp[i][0] = newL
                            dp[i][1] = dp[j][1]
                        elif newL == dp[i][0]:
                            dp[i][1] += dp[j][1]
                            
                if dp[i][0] in count:
                    count[dp[i][0]] += dp[i][1]
                else:
                    count[dp[i][0]] = dp[i][1]
                        
                maxL = max(maxL, dp[i][0])
                
        #print(dp)
        #print(count)
        return count[maxL]
                
                
