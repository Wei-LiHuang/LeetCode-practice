class Solution:
    
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        
        n = len(a)
        left = 0
        right = 0
        cur = a[left]
        res = 0        
        
        while left < n:                        
            
            while right < n - 1 and cur * a[right + 1] < k:                
                right += 1        
                cur *= a[right]
                
            res += (right - left + 1)
            
            cur /= a[left]
            left += 1
            
        
        return res
            
            
            
            
