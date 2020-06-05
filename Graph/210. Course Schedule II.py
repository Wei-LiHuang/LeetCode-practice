#[目標][先修] -> 會得到反向的拓樸排序 -> 反轉edges
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        
        def topologicalSort(cur, edges, visited, hasCircle, path):
            
            if cur in hasCircle:
                return hasCircle[cur]
            
            if cur in visited:
                hasCircle[cur] = True
                return True
            
            visited.add(cur)
            
            if cur in edges:
                neighbors = edges[cur]

                for neighbor in neighbors:
                    if topologicalSort(neighbor, edges, visited, hasCircle, path):
                        hasCircle[cur] = True
                        return True
                
            path.append(cur)
            
            hasCircle[cur] = False
            return False
        
        path = []
        
        #reverse edges:
        edges = dict()
        for pair in prerequisites:
            tar = pair[1]
            pre = pair[0]
            if pre in edges:
                edges[pre].append(tar)
            else:
                edges[pre] = [tar]
                
        visited, hasCircle = set(), dict()
        for i in range(0, n):
            if topologicalSort(i, edges, visited, hasCircle, path):
                return []
            
        return path
            
            
        
