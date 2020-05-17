# bill: 5, 10, 20
# received 5: five += 1
# received 10: ten += 1, five -= 1 
# received 20: twenty += 1, if ten > 0: ten -= 1, five -= 1 else: five -= 3
# O(n)


class Solution(object):
    
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        twenty = 0
        
        for b in bills:
            
            if b == 5:
                five += 1
            
            if b == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            
            if b == 20:
                
                if ten >= 1:
                    if five < 1:
                        return False
                    else:
                        ten -= 1
                        five -= 1
                        twenty += 1
                else:
                    if five < 3:
                        return False
                    else:
                        five -= 3
                        
        return True
