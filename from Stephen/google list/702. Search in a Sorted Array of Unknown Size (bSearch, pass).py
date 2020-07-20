class Solution:
    def search(self, reader, tgt):
        """
        :type reader: ArrayReader
        :type tgt: int
        :rtype: int
        """
        # find the r, where reader.get(r) >= tgt
        l, r = 0, 1
        
        while reader.get(r) < tgt:
            r *= 2
            
        # now we get a range from l to r:
        while l <= r:
            
            if l == r:
                if reader.get(l) == tgt:
                    return l
                else:
                    return -1
                
            elif l == r - 1:
                if reader.get(l) == tgt:
                    return l
                elif reader.get(r) == tgt:
                    return r
                else:
                    return -1
            else:  
                mid = (l + r) // 2
                if reader.get(mid) == tgt:
                    return mid
                elif reader.get(mid) < tgt:
                    l = mid + 1
                    continue
                elif reader.get(mid) > tgt:
                    r = mid - 1
                    continue
                    
        return -1
