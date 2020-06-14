# 1.use hash map + DFS
# 2. try not unsing hash map

class Solution:
    
    def permuteUnique(self, a: List[int]) -> List[List[int]]:
                
        def dfs(a, path, res, visited, tgt, check):
            
            n = len(path)
            
            if n == tgt:
                _str = str(path)
                if _str not in check:
                    l = list(path)
                    res.append(l)
                    check.add(_str)
                return
            
            for i in range(0, len(a)):                
                if i not in visited:
                    path.append(a[i])
                    visited.add(i)
                    dfs(a, path, res, visited, tgt, check)
                    path.pop()
                    visited.remove(i)
                    
            return
        
        visited, check = set(), set()
        res = []
        dfs(a, [], res, visited, len(a), check)
        
        return res
