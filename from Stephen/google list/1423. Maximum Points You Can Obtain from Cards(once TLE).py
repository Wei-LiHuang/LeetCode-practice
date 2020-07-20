class Solution:
    
    def maxScore(self, a: List[int], k: int) -> int:        
        '''
            total sum = a[0] + a[1] + ... + a[n - 1]
            
            if k >= n:
                return total sum
                
            else:
                leftSum = a[0] + a[1] + ... + a[i - 1]
                rightSum = a[j + 1] + a[j + 2] + ... + a[n - 1]
                
                where a[i], a[i + 1], ..., a[j] is the card we cannot take
                and dis = (j - i + 1) = n - k
                                                            
                res = max(total sum - (leftSum + rightSum))
                    = totalSum - max(leftSum + rightSum)
                    = totalSum - min(sum(i to j))                
        '''
        n = len(a)
        
        totalSum = sum(a)
        if k >= n:
            return totalSum
        
        windowSize = n - k
        r, windowSum = n - k - 1, 0
        # create the first window:
        for i in range(0, r + 1):
            windowSum += a[i]
            
        res = totalSum - windowSum
        for l in range(1, n):
            windowSum -= a[l - 1]
            r += 1            
            if r == n:
                break            
            windowSum += a[r]
            res = max(res, totalSum - windowSum)
                        
        return res
        
                                                
    def maxScore_TLE(self, a: List[int], k: int) -> int:
        
        '''
            DP(1,2,3,4,5,6,1) => 1 + DP(2,3,4,5,6,1) or 1 + DP(1,2,3,4,5,6) -> 1 + 7 or 1 + 11 -> 12 -> res = 12
            
            DP(2,3,4,5,6,1) => 2 + DP(3,4,5,6,1) or 1 + DP(2,3,4,5,6) -> 2 + 3 or 1 + 6 -> 7
            DP(1,2,3,4,5,6) => 1 + DP(2,3,4,5,6) or 6 + DP(1,2,3,4,5) -> 1 + 6 or 6 + 5 -> 11
            
            DP(3,4,5,6,1) => 3 + DP(4,5,6,1) or 1 + DP(3,4,5,6) -> 3
            DP(2,3,4,5,6) => 2 + DP(3,4,5,6) or 6 + DP(2,3,4,5) -> 6
            DP(1,2,3,4,5) => 1 + DP(2,3,4,5) or 5 + DP(1,2,3,4) -> 5                                                
            
            
            dp[i][j]:
                DP(3,4,5,6,1) = dp[2][6] = max(3, 1) = 3
                
            if j - i + 1 <= (n - k) -> dp[i][j] = 0
                j <= n - k - 1 + i                                                                             
        '''                       
        n = len(a)
        if k >= n:
            return sum(a)
                
        dp = []
        for i in range(0, n):
            dp.append([0] * n)
                        
        for i in range(n - 1 - k, -1, -1):
            for j in range(i, n):                
                if j - i + 1 <= (n - k):
                    dp[i][j] = 0                                    
                else:                    
                    dp[i][j] = max(a[i] + dp[i + 1][j], a[j] + dp[i][j - 1])
                    #print([i, j, dp[i][j]])
                    
                            
        return dp[0][n - 1]
        
