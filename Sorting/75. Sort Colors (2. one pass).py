class Solution:
    
    def sortColors(self, a: List[int]) -> None:
                
        n = len(a)        
        if n <= 1:
            return
        
        #n >= 2
        p0 = 0
        p2 = n - 1        
        i = 0
        while i <= p2:            

            if a[i] == 2:
                a[i], a[p2] = a[p2], 2
                p2 -= 1    
            else:
                if a[i] == 0:
                    a[i], a[p0] = a[p0], 0
                    p0 += 1    
                
                i += 1                                                                                                         
        return 
        
    
    
