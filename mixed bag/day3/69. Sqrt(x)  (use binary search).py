class Solution:
    def mySqrt(self, x: int) -> int:
        
        def rec(l, r, x):
            d = r - l + 1            
            if d == 2:                    
                return l
            if d == 3:
                mid = l + 1
                if mid * mid <= x:
                    return mid
                else:
                    return l                        

            mid = (l + r) // 2            
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            if mid * mid < x and (mid + 1) * (mid + 1) >= x:
                return mid + 1
            if (mid + 1) * (mid + 1) < x:
                return rec(mid + 1, r, x)
            if mid * mid > x:
                return rec(l, mid, x)

            return None
            
        if x <= 1:
            return x
            
        return rec(1, x, x)
                
            
            
