#check each point on the side lane:

class Solution:
    
    def pacificAtlantic(self, a: List[List[int]]) -> List[List[int]]:
        
        def dfs(a, r, c, _set):
            
            m, n = len(a), len(a[0])
            
            index = r * n + c            
            if index in _set:
                return
            
            _set.add(index)
            
            #up:
            if r > 0 and a[r][c] <= a[r - 1][c]:
                dfs(a, r - 1, c, _set)
            
            #down:
            if r < m - 1 and a[r][c] <= a[r + 1][c]:
                dfs(a, r + 1, c, _set)            
            
            #right:
            if c < n - 1 and a[r][c] <= a[r][c + 1]:
                dfs(a, r, c + 1, _set)            
            
            #left:
            if c > 0 and a[r][c] <= a[r][c - 1]:
                dfs(a, r, c - 1, _set)            
            
            return
            
        #edge case:
        m = len(a)
        if m == 0:
            return []
        n = len(a[0])
        if n == 0:
            return []
                                
        inP, inA = set(), set()
        
        for c in range(0, n):
            dfs(a, 0, c, inP)
            dfs(a, m - 1, c, inA)
        for r in range(0, m):
            dfs(a, r, 0, inP)
            dfs(a, r, n - 1, inA)
        
        res = []
        for p in inP:
            if p in inA:
                res.append([p // n, p % n])
                
        return res
            
        
        
