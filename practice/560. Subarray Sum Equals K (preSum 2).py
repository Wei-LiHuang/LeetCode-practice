class Solution:
    
    def subarraySum(self, a: List[int], k: int) -> int:
        
        n = len(a)
        
        preSum = dict()
        preSum[0] = 1
        curSum = 0
        res = 0
        for i in range(0, n):
            curSum += a[i]            
            if curSum - k in preSum:
                res += (1 * preSum[curSum - k])
                
            if curSum in preSum:
                preSum[curSum] += 1
            else:
                preSum[curSum] = 1
                
        return res
                
                
                
            
        
