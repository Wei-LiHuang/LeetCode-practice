class Solution:
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def hasCircleF(g, cur, visited, hasCircle):            
            
            if cur in hasCircle:
                return hasCircle[cur]
            
            if cur in visited:
                hasCircle[cur] = True
                return True
            
            visited.add(cur)
                        
            for neighbor in g[cur]:
                if (hasCircleF(g, neighbor, visited, hasCircle)):
                    hasCircle[cur] = True
                    return True
            
            hasCircle[cur] = False
            return False
        
        
        visited, hasCircle, res = set(), dict(), []
        
        for i in range(0, len(graph)):
            if not hasCircleF(graph, i, visited, hasCircle):
                res.append(i)
        
        return res
            
            

        
        
