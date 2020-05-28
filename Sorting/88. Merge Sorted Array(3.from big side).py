class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        i1, i2, cur = m - 1, n - 1, -1
        
        if n == 0:
            return
        
        for i in range(len(a) - 1, -1, -1):
            
            if i1 >= 0 and i2 >= 0:                
                if a[i1] >= b[i2]:
                    a[i] = a[i1]
                    i1 -= 1
                else:
                    a[i] = b[i2]
                    i2 -= 1
            else:
                cur = i
                break
                
        if i1 >= 0:
            for j in range(cur, -1, -1):
                a[j] = a[i1]
                i1 -= 1
        if i2 >= 0:
            for j in range(cur, -1, -1):
                a[j] = b[i2]
                i2 -= 1
                
        return
        
        

        
