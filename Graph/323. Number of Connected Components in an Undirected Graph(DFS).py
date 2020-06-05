class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(g, index, remain):                                                            
            remain.remove(index)
            if index in g:
                neighbors = g[index]
                for n in neighbors:
                    if n in remain:
                        dfs(g, n, remain)
            return
                                                                                
        g = dict()        
        for pair in edges:            
            v1 = pair[0]
            v2 = pair[1]
            if v1 in g:
                g[v1].append(v2)
            else:
                g[v1] = [v2]
            
            if v2 in g:
                g[v2].append(v1)
            else:
                g[v2] = [v1]
            
        remain = set()
        for i in range(0, n):
            remain.add(i)
        
        count = 0
        for i in range(0, n):
            if i in remain:
                dfs(g, i, remain)
                count += 1
            else:
                continue
        
        return count
