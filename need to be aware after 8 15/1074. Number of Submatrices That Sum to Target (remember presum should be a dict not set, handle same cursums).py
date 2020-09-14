class Solution:
    
    def numSubmatrixSumTarget(self, a: List[List[int]], tgt: int) -> int:
        '''
            1. one Dim:                
                curSum = a[0] + ... + a[j]
                sum(i, j) = a[i] + ... + a[j] = curSum - preSum[i - 1]
                if sum(i, j) == tgt -> curSum = tgt + preSum[i - 1] -> if curSum - tgt in preSum (= preSum[i - 1]) -> res += 1
            
            2. two Dim:
                curSum = sum(leftTop = a[0][0], rightBot = a[r2][c2])
                sum of sub matrix = sum(leftTop = a[r1][c1], rightBot = a[r2][c2]), 0 <= r1 <= r2, 0 <= c1 <= c2)
                -> sum(r1,c1,r2,c2) = sum(0,0,r2,c2) - sum(0,0,r2,c1-1) - sum(0,0,r1-1,c2) + sum(0,0,r1-1,c1-1)
                -> curSum = sum(0,0,r2,c2) -> if curSum - tgt = sum(0,0,r2,c1-1) + sum(0,0,r1-1,c2) - sum(0,0,r1-1,c1-1), res += 1
                -> BUT WE CANT GET (sum(0,0,r2,c1-1) + sum(0,0,r1-1,c2) - sum(0,0,r1-1,c1-1)) IN O(1) LIKE one Dim problem
            
            3. from 1504. Count Submatrices With All Ones:                
                for r1 in range(0, m):
                    for r2 in range(r1, m):                    
                        -> we now get a one dim matrix: A
                        -> A[c] = a[r1][c] + ... + a[r2][c]
                        and we can apply one dim method for A                                                
        '''
        m = len(a)
        n = len(a[0])
        
        res = 0
        for r1 in range(0, m):
            A = a[r1][:]                                                
            for r2 in range(r1, m):                                
                if r2 > r1:
                    for c in range(0, n):                
                        A[c] += a[r2][c]
                
                preSum = dict()
                preSum[0] = 1
                curSum = 0
                for c in range(0, n):
                    curSum += A[c]
                    if curSum - tgt in preSum:
                        res += preSum[curSum - tgt]                        
                    
                    if curSum in preSum:
                        preSum[curSum] += 1
                    else:
                        preSum[curSum] = 1
                    
        
        return res
