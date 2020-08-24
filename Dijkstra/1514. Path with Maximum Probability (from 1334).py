class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        # 1. build graph with weight
        path = dict()        
        for i in range(0, len(edges)):
            v1, v2, prob = edges[i][0], edges[i][1], succProb[i]
            if v1 not in path:
                path[v1] = dict()            
            if v2 not in path:
                path[v2] = dict()                                
            path[v1][v2] = [prob, v2]
            path[v2][v1] = [prob, v1]
            
        # 2. use heap to get the max prob next step:
        visited = dict()
        
        maxHeap = [[1 * -1, start]]
        while len(maxHeap) > 0:
            pop = heapq.heappop(maxHeap)            
            curNode, curP = pop[1], (pop[0] * -1)            
            if curNode not in visited:
                visited[curNode] = curP
            
            if curNode in path:
                for key in path[curNode].keys():                    
                    neighbor, neighborP = path[curNode][key][1], curP * path[curNode][key][0]                    
                    if neighbor not in visited:
                        heapq.heappush(maxHeap, [neighborP * -1, neighbor])
        
        # 3. get ans:
        if end in visited:
            return visited[end]
        else:
            return 0
                
