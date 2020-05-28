class Solution:
    
    def findMin(self, a: List[int]) -> int:
        
        n = len(a)
        
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        
        l, r = 0, n - 1
        
        while a[l] > a[r]:
            
            if (r - l) == 1:
                return min(a[l], a[r])
            
            mid = int((l + r) / 2)
            
            if a[mid] > a[l]:
                l = mid + 1            
            else:
                r = mid
                
        return a[l]
            
        
