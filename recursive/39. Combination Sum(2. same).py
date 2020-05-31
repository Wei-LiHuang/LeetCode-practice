class Solution:
    
    def combinationSum(self, a: List[int], target: int) -> List[List[int]]:
        
        def dfs(a, index, tgt, path, res):
            
            if a[index] > tgt:
                return            
            elif a[index] == tgt:
                path.append(a[index])                
                res.append(list(path))
                path.pop()
                return
            else:                
                path.append(a[index])
                for i in range(index, len(a)):
                    dfs(a, i, tgt - a[index], path, res)
                path.pop()
                return
            
        res = []
        a.sort()
        
        for i in range(0, len(a)):
            dfs(a, i, target, [], res)
        
        return res
        
        
        
        
