# can use a element repeatedly
class Solution:
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(a:List[int], start:int, path: List[int], tgt: int, res: List[List[int]]):
                        
            if a[start] > tgt:                
                return
                
            elif a[start] == tgt:
                path.append(a[start])
                r = list(path)
                res.append(r)
                path.pop()
                return #no zeros
            
            else:
                tgt -= a[start]
                path.append(a[start])
                
                for i in range(start, len(a)):
                    dfs(a, i, path, tgt, res)
                                    
                path.pop()
                    
                return                                                                                                                                                    
        
        
        candidates.sort()
        n, res = len(candidates), []        
        for i in range(0, n):            
            path = []
            dfs(candidates, i, path, target, res)
        
        return res
