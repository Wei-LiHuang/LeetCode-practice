class Solution:
    
    def findPeakElement(self, a: List[int]) -> int:
        
        if len(a) <= 1:
            return 0
        
        l, r = 0, len(a) - 1
        
        while l < r:                        
            mid = (l + r) // 2
            
            if a[mid] > a[mid + 1]:
                r = mid
            else:
                l = mid + 1
                
            if l == r:
                return l
            
        return -1
            
        
