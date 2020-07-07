class Solution:
    
    def findPeakElement(self, a: List[int]):
        
        def rec(a, l, r):
            if l == r:
                return l
            
            elif l == r - 1:
                if a[l] > a[r]:
                    return l
                else:
                     return r                            
            else:
                mid = (l + r) // 2
                
                if a[mid] > a[mid - 1]:
                    return rec(a, mid, r)
                
                elif a[mid] < a[mid - 1]:
                    return rec(a, l, mid - 1)
                
            return -1
            
        if len(a) == 0:
            return 0
        
        res = rec(a, 0, len(a) - 1)
        return res
