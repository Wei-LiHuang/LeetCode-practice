# dfs, no repeat element

class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
                
        def dfs(a, path, tgtL, visited, res, s):
            if len(path) == tgtL:
                l = list(path)
                res.append(l)
                return
            
            for i in range(s, len(a)):
                if i not in visited:
                    visited.add(i)
                    path.append(a[i])
                    dfs(a, path, tgtL, visited, res, i + 1)
                    path.pop()
                    visited.remove(i)                    
            return
                            
        a = []
        for i in range(1, n + 1):
            a.append(i)
            
        path = []
        tgtL = k
        visited = set()
        res = []
        dfs(a, path, tgtL, visited, res, 0)
        
        return res
        
