class Solution:
    
    def maxSideLength(self, a: List[List[int]], threshold: int) -> int:
        
        def getSquareSum(preSum, i, j, l):                                                
            res = 0
            m, n = len(preSum), len(preSum[0])                     
            
            index = i * n + j
            if index in memo and l in memo[index]:
                return memo[index][l]
                        
            r1, r2, c1, c2 = i, i + l, j, j + l
            res = preSum[r2][c2] - preSum[r1][c2] - preSum[r2][c1] + preSum[r1][c1];
                                   
            if index not in memo:
                memo[index] = dict()
            memo[index][l] = res                    
            return res
                                
        m = len(a)
        n = len(a[0])        
        preSum = []
        for i in range(0, m + 1):
            preSum.append([0] * (n + 1))
        
        _sum = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + a[i-1][j-1]
                
        memo = dict()                
        
        res = 0
        for i in range(0, m):
            for j in range(0, n):                
                l, r = 1, min(m - i, n - j)                                                
                while l <= r:              
                    
                    if getSquareSum(preSum, i, j, r) <= threshold:
                        res = max(res, r)                    
                        break
                
                    if l == r and getSquareSum(preSum, i, j, l) <= threshold:
                        res = max(res, l)
                        break
                    elif l == r - 1:
                        if getSquareSum(preSum, i, j, r) <= threshold:
                            res = max(res, r)
                        elif getSquareSum(preSum, i, j, l) <= threshold:
                            res = max(res, l)                            
                        break
                    else:                    
                        mid = (l + r) // 2                        
                        if getSquareSum(preSum, i, j, mid) <= threshold:
                            l = mid
                        else:
                            r = mid - 1                
        return res                
            
    def maxSideLength_TLE(self, a: List[List[int]], threshold: int) -> int:
        
        def getSquareSum(preSum, i, j, l):                                                
            res = 0
            m, n = len(preSum), len(preSum[0])                     
            
            index = i * n + j
            if index in memo and l in memo[index]:
                return memo[index][l]
                        
            r1, r2, c1, c2 = i, i + l - 1, j, j + l - 1
            for r in range(r1, r2 + 1):
                if r == 0 and c1 == 0:
                    res += preSum[r][c2]
                elif c1 == 0:
                    res += preSum[r][c2] - preSum[r - 1][n - 1]
                else:
                    res += preSum[r][c2] - preSum[r][c1 - 1]                    
                    
            if index not in memo:
                memo[index] = dict()
            memo[index][l] = res                    
            return res
                                
        m = len(a)
        n = len(a[0])        
        preSum = []
        for i in range(0, m):
            preSum.append([0] * n)
        
        _sum = 0
        for i in range(0, m):
            for j in range(0, n):
                _sum += a[i][j]
                preSum[i][j] = _sum
        
        
        memo = dict()                
        
        res = 0
        for i in range(0, m):
            for j in range(0, n):                
                l, r = 1, min(m - i, n - j)                                                
                while l <= r:              
                    
                    if getSquareSum(preSum, i, j, r) <= threshold:
                        res = max(res, r)                    
                        break
                
                    if l == r and getSquareSum(preSum, i, j, l) <= threshold:
                        res = max(res, l)
                        break
                    elif l == r - 1:
                        if getSquareSum(preSum, i, j, r) <= threshold:
                            res = max(res, r)
                        elif getSquareSum(preSum, i, j, l) <= threshold:
                            res = max(res, l)                            
                        break
                    else:                    
                        mid = (l + r) // 2                        
                        if getSquareSum(preSum, i, j, mid) <= threshold:
                            l = mid
                        else:
                            r = mid - 1                
        return res                
                    
                                                                
                
        
        
