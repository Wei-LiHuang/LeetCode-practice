class Solution:
    
    def productExceptSelf(self, a: List[int]) -> List[int]:
        '''
            [1,2,3,4]                    
            p0 = [] * [2,3,4]
            p1 = [1] * [3, 4]
            p2 = [1,2] * [4]
            p3 = [1,2,3] * []                        
        '''
        if len(a) == 0:
            return 0
        
        n = len(a)
        l = [1] * n
        r = [1] * n
        
        for i in range(0, n):            
            if i == 0:
                continue
            l[i] *= a[i - 1] * l[i - 1]
        
        for i in range(n - 1, -1, -1):            
            if i == n - 1:
                continue
            r[i] *= a[i + 1] * r[i + 1]
            
        res = [1] * n
        for i in range(0, n):
            res[i] = l[i] * r[i]
            
        return res
        
