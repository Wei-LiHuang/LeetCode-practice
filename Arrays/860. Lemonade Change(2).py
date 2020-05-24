class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        t5, t10, t20 = 0, 0, 0
        
        for b in bills:
            
            if b == 5:
                t5 += 1
                
            elif b == 10:
                if t5 == 0:
                    return False
                else:
                    t5 -= 1
                    t10 += 1
                    
            elif b == 20:
                    
                    if t10 > 0 and t5 > 0:
                        t20 += 1
                        t10 -= 1
                        t5 -= 1
                    elif t5 >= 3:
                        t5 -= 3
                        t20 += 1
                    else:
                        return False
    
    
        return True
