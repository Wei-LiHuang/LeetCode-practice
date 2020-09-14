class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        
        # 1. build edges:
        edges = dict()
        for pair in relations:
            '''
                [1, 3] means take x -> then take y
                so the graph should be x -> y
                reverse: y -> x                                                
            '''
            if pair[1] not in edges:
                edges[pair[1]] = list()
            edges[pair[1]].append(pair[0])
                
        #print(edges)
        
        # 2.detect cycle:                
        def detect(cur, edges, visited, hasCycle, path):
            
            if cur in hasCycle:
                return hasCycle[cur]
            if cur in visited:
                hasCycle[cur] = True
                return True
            
            visited.add(cur)
            if cur in edges:
                for neighbor in edges[cur]:
                    if detect(neighbor, edges, visited, hasCycle, path):
                        hasCycle[cur] = True
                        return True
                        
            path.append(cur + 1)
            hasCycle[cur] = False
            return False       
        
        hasCycle, visited, path = dict(), set(), []
        for i in range(0, N):
            if detect(i, edges, visited, hasCycle, path):
                return -1
                    
        # 3. count group:
        #print(path)
                
        cToG = dict()
        res = -1        
        for i in path:                        
            if i in edges:
                preOfI = edges[i] 
                maxG = 0
                for pre in preOfI:                    
                    maxG = max(maxG, cToG[pre])
                cToG[i] =  maxG + 1
            else:
                cToG[i] = 1
                
            res = max(res, cToG[i]) 
            
        return res
