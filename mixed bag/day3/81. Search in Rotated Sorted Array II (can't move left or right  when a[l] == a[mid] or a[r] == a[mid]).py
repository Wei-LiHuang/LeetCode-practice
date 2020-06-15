# can't make decision when a[l] == a[mid] or a[r] == a[mid]

class Solution:
    
    def search(self, a: List[int], tgt: int) -> bool:
        
        
        def bSearch(a, tgt, l, r):
            
            if l == r:
                return a[l] == tgt
            
            if l == r - 1:
                return a[l] == tgt or a[r] == tgt
            
            mid = (l + r) // 2
            
            if a[mid] == tgt:
                return True
            
            if a[mid] > tgt:
                return bSearch(a, tgt, l , mid - 1)
            
            if a[mid] < tgt:
                return bSearch(a, tgt, mid + 1, r)
            
                                        
        def bSearchInRotatedArray(a, tgt, l, r):
            
            if l == r:
                return a[l] == tgt            
            
            if l == r - 1:
                return a[l] == tgt or a[r] == tgt            
            
            mid = (l + r) // 2
            
            # this is the key
            if a[mid] == a[l]:
                return bSearchInRotatedArray(a, tgt, l + 1, r) 
            
            # this is the key
            if a[mid] == a[r]:
                return bSearchInRotatedArray(a, tgt, l, r - 1)
            
            if a[mid] > a[l]:                                                                                    
                if tgt <= a[mid] and tgt >= a[l]:
                    return bSearch(a, tgt, l , mid)
                else:
                    return bSearchInRotatedArray(a, tgt, mid , r)
            
            if a[mid] < a[r]:
                if tgt >= a[mid] and tgt <= a[r]:
                    return bSearch(a, tgt, mid , r)
                else:
                    return bSearchInRotatedArray(a, tgt, l, mid)
            
        n = len(a)
        if n == 0:
            return False
        
        l, r = 0, n - 1
        
        if a[l] < a[r]:
            return bSearch(a, tgt, l, r)
        else:
            return bSearchInRotatedArray(a, tgt, l, r)
