class Solution:
    
    def majorityElement(self, a: List[int]) -> List[int]:
            
        n = len(a)    
        
        if n == 0:
            return []
               
        cur1 = a[0]
        count1 = 1
        
        cur2 = -1
        count2 = 0
        
        start = -1
        for i in range(1, n):
            if a[i] == a[i - 1]:
                count1 += 1
            else:
                cur2 = a[i]
                count2 = 1
                start = i + 1
                break
                
        for i in range(start, n):
            
            if a[i] == cur1:
                count1 += 1                                                              
            elif a[i] == cur2:
                count2 += 1                             
            else:                
                count1 -= 1                                                                                                                
                count2 -= 1
                
                if count2 < 0:
                    cur2 = a[i]
                    count2 = 1

                elif count1 < 0:
                    cur1 = a[i]
                    count1 = 1
                
        res = []
        count1 = 0
        for i in range(0, n):
            if a[i] == cur1:
                count1 += 1
        
        count2 = 0
        for i in range(0, n):
            if a[i] == cur2:
                count2 += 1                

        if count1 > n // 3:
            res.append(cur1)
            
        if count2 > n // 3:
            res.append(cur2)
                    
        return res
