class Solution:
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        def dfs(cur, neighbors, visited, hasCircle, path):
            
            if cur in hasCircle:
                return hasCircle[cur]
            if cur in visited:
                hasCircle[cur] = True
                return True
            
            visited.add(cur)
            
            if cur in neighbors:
                for neighbor in neighbors[cur]:
                    if dfs(neighbor, neighbors, visited, hasCircle, path):
                        hasCircle[cur] = True
                        return True
                
            path.append(cur)
            hasCircle[cur] = False
            return False
            
                            
        neighbors = dict()
        
        for pair in prerequisites:            
            start = pair[0] # reversed
            end = pair[1] # reversed
            if start in neighbors:
                neighbors[start].append(end)
            else:
                neighbors[start] = [end]
        
        path, visited, hasCircle = [], set(), dict()
        for i in range(0, numCourses):
            if dfs(i, neighbors, visited, hasCircle, path):
                return []
            
        return path
