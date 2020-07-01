class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def dfs(d, path, res, curSum, k, n):
            
            if len(path) == k and curSum == n:
                res.append(path[:])
                return
            
            for i in d.keys():
                
                if len(path) == 0:                                    
                    path.append(i)
                    d[i] -= 1
                    dfs(d, path, res, curSum + i, k, n)
                    path.pop()
                    d[i] += 1
                else:
                    if d[i] > 0 and i > path[-1]:
                        path.append(i)
                        d[i] -= 1
                        dfs(d, path, res, curSum + i, k, n)
                        path.pop()
                        d[i] += 1
            return
        
        
        d = dict()
        for i in range(1, 10):            
            d[i] = 1
            
        res = []
        dfs(d, [], res, 0, k, n)
        
        return res
        
        
