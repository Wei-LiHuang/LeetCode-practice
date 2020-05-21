class Solution:
    def longestMountain(self, a: List[int]) -> int:
        
        n = len(a)
        left = [0] * n
        right = [0] * n
        
        for i in range(n - 2, 0, -1):             
            if a[i] > a[i + 1]:
                right[i] = right[i + 1] + 1
                                    
        for i in range(1, n):            
            if a[i] > a[i - 1]:
                left[i] = left[i - 1] + 1
        
        _max = 0
        for i in range(0, n):
            if left[i] > 0 and right[i] > 0:
                _max = max(_max, left[i] + right[i] + 1)
        
        return _max
            
