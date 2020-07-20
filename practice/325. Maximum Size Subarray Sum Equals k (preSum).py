class Solution:
    
    def maxSubArrayLen(self, a: List[int], k: int) -> int:
        '''
        let Si = a0 + a1 + ... + ai
            Sj = a0 + a2 + ... + aj
            
        then a[i + 1] + a[i + 2] + ... + a[j] = Sj - Si
        if Sj - Si == k:
            update res
        
        if Sj not in preSum:
            preSum[Sj] = j
            
        # because we want maximum length
                   
        '''
        
        n = len(a)
        
        if sum(a) == k:
            return len(a)
        
        preSum = dict()
        preSum[0] = -1
        curSum = 0
        res = 0
        for i in range(0, n):            
            curSum += a[i]            
            if (curSum - k) in preSum:
                j = preSum[curSum - k]
                res = max(res, i - j)
                
            if curSum not in preSum:
                preSum[curSum] = i                                                                                    
                
        return res
