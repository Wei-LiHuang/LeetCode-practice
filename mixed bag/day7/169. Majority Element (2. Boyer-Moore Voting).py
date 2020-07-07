class Solution:
    
    def majorityElement(self, a: List[int]) -> List[int]:
        
        n, v1, c1, v2, c2 = len(a), 0, 0, 0, 0        
        for i in range(0, n):
            if a[i] == v1:
                c1 += 1
            elif a[i] == v2:
                c2 += 1
            elif c1 == 0:
                v1 = a[i]
                c1 = 1
            elif c2 == 0:
                v2 = a[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        res = []
        c1 = 0
        for i in a:
            if i == v1:
                c1 += 1
        if c1 > n // 3:
            res.append(v1)
            
        c2 = 0
        for i in a:
            if i == v2:
                c2 += 1
        if c2 > n // 3 and v2 != v1:
            res.append(v2)
            
        return res
