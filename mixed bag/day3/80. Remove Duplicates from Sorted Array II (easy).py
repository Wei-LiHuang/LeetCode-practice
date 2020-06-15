class Solution:
    
    def removeDuplicates(self, a: List[int]) -> int:
        
        if len(a) <= 2:
            return len(a)
        
        l, n = -1, len(a)        
        count = 0
        
        for i in range(0, n):            
            if i == 0:
                l = 1
                count = 1
                continue
                
            if i > 0:                
                if a[i] == a[i - 1]:                    
                    if count == 1:
                        a[l] = a[i]
                        l += 1
                        count = 2
                        
                    elif count > 1:
                        count = 2
                        continue
                                                            
                elif a[i] != a[i - 1]:                    
                    a[l] = a[i]
                    l += 1
                    count = 1
            
        return l
            
