class Solution(object):
    
    def numSubarrayProductLessThanK(self, a, k):
        
        l = 0
        r = 0
        n = len(a)                
        res = 0
        curProduct = a[l]

        while l < n: # cause n loop
            
            # move r
            if r < l:
                r = l
                curProduct = a[l]
                        
            while r < n - 1 and curProduct < k:                            
                r += 1
                curProduct *= a[r]
                if curProduct >= k:
                    curProduct /= a[r]
                    r -= 1                    
                    break                                    
                
            # starting from l to r is a local max sub-seq:
            if curProduct < k:
                _len = r - l + 1
                res += _len            
                
            # move l:
            curProduct /= a[l]            
            l += 1                            
            
        return res    
