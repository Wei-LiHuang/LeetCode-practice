class Solution:
    
    def orangesRotting(self, a: List[List[int]]) -> int:
        
        def willRot(r, c, a):            
            m = len(a)
            n = len(a[0])                             
            #up:            
            if r > 0 and a[r - 1][c] == 2:
                return True                                                                            
            #down:            
            if r < m - 1 and a[r + 1][c] == 2:
                return True            
            #left:
            if c < n - 1 and a[r][c + 1] == 2:
                return True        
            #right
            if c > 0 and a[r][c - 1] == 2:
                return True
        
            return False

        m = len(a)
        n = len(a[0])         
        
        fresh = []
        
        for r in range(0, m):            
            for c in range(0, n):
                if a[r][c] == 1:
                    fresh.append(r * n + c)    
        
        if len(fresh) ==  0:
            return 0
        
        res = 0
        while len(fresh) > 0:
            curSize = len(fresh)
            stillFresh = []
            rot = []
            for i in range(0, curSize):
                cur = fresh.pop()
                if willRot(cur // n, cur % n, a):
                    rot.append(cur)
                else:
                    stillFresh.append(cur)
            
            if len(stillFresh) == curSize:
                return -1
            
            for r in rot:
                a[r // n][r % n] = 2
        
            res += 1
            fresh = stillFresh
            
        
        return res
        
            
            
                    
