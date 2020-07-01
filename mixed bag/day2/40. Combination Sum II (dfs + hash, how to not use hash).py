# sol1: hash map

# sol2: skip same a[index] (but need to perform once... line 18)

class Solution:
    
    def combinationSum2(self, a: List[int], tgt: int) -> List[List[int]]:
                
        def dfs(a, tgt, s, curSum, path, res):
                                
            if curSum == tgt:
                res.append(list(path))
                return
            
            if curSum < tgt:                
                for i in range(s + 1, len(a)):
                    if i > (s + 1) and a[i] == a[i - 1]:
                        continue                                                        
                    if curSum + a[i] <= tgt:
                        path.append(a[i])
                        dfs(a, tgt, i, curSum + a[i], path, res)
                        path.pop()
                    
                return
            
        a.sort()
        pSet, res = set(), []
        dfs(a, tgt, -1, 0, [], res)
        
        return res
                        
                    
                
