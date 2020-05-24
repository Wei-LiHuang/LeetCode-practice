class Solution:
    def merge(self, a1: List[int], l1: int, a2: List[int], l2: int) -> None:
        
        if l2 == 0:
            return 
        
                
        p1 = l1 - 1
        p2 = l2 - 1
        
        for i in range(l1 + l2 - 1, -1, -1):
            
            if a1[p1] > a2[p2]:
                a1[i] = a1[p1]
                p1 -= 1
            else:
                a1[i] = a2[p2]
                p2 -= 1
            
            if p1 < 0 or p2 < 0:
                break
        
        if p2 >= 0:
            for j in range (p2, -1, -1):
                a1[j] = a2[p2]
                p2 -= 1
            
        return
