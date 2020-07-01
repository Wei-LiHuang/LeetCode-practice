    def mySqrt(self, x: int) -> int:
        
        def rec(l, r, tgt):
            
            #print([l, r, tgt])
            
            if l == r:
                return l

            mid = (l + r) // 2
            
            #print(mid)
            
            if mid * mid <= tgt and (mid + 1) * (mid + 1) > tgt:
                return mid
            
            elif mid * mid > tgt:
                return rec(l, mid, tgt)
            
            elif (mid + 1) * (mid + 1) <= tgt:
                return rec(mid + 1, r, tgt)
                                                    
        if x <= 1:
            return x
        
        return rec(1, x, x)
