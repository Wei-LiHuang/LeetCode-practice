class Solution:
    def minSubArrayLen(self, tgt: int, a: List[int]) -> int:
        
        curSum, l, res, n = 0, 0, float('inf'), len(a)
        
        for r in range(0, n):                                                
            if l == r:
                curSum = a[l]
                if curSum >= tgt:
                    res = min(res, 1)
                    l += 1
            
            elif l < r:
                curSum += a[r]
                if curSum >= tgt:                    
                    while curSum >= tgt:
                        res = min(res, r - l + 1)
                        curSum -= a[l]
                        l += 1
                    
                    
        if res == float('inf'):
            return 0
                
        return res
