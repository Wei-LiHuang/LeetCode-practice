class Solution:
    def numSubarrayProductLessThanK(self, a: List[int], k: int) -> int:
        
        left, n, cur, res = 0, len(a), 1, 0
        for i in range(0, n):
            cur *= a[i]            
            while cur >= k:
                cur /= a[left]
                left += 1 
                if left == n:
                    return res
                
            res += (i - left + 1)
        
        return res
            
            
        
