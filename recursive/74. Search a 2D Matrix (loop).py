class Solution:
    
    def searchMatrix(self, a: List[List[int]], tgt: int) -> bool:
        
        m = len(a)
        if m == 0:
            return False    
        n = len(a[0])
                
        left, right = 0, (m * n - 1)
        
        while left <= right:
            lr, lc, rr, rc = int(left/n), left % n, int(right/n), right % n            
            mid = int((left + right) / 2)
            mr, mc = int(mid/n), mid % n
            
            if tgt == a[mr][mc]:
                return True
            else:
                if tgt > a[mr][mc]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
                                            
        return False
            
            
