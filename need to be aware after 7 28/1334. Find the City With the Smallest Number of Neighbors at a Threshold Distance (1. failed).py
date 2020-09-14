class Solution:
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:                
        '''
            find the cities with the smallest number of neighbors
            
            1. calculate all the min distance between all the cities -> O(n^2)
               then for each city, check how many neighbors there are in the dis smaller then distanceThreshold -> O(N ^ 2)               
               -> O(N^2) algorithm 
               
               -> wrong, no way to handle longer path with smaller weight sum
                (we'll need visited to avoid inner loop in dfs, but that also delete the ans of longer path with smaller sum)
                
            2. use Dijkstra: 
                can watch this vid: https://www.youtube.com/watch?v=9wV1VxlfBlI                
                like BFS, but the q is replaced by the heap                
        '''
        
        # get the "min weight sum path" from cur to each other nodes:
        def Dijkstra(n, path, cur, memo):            
            minHeap = []            
            #1. put the starting point to heap:
            minHeap.append([0, cur])
            #2. do the bfs:
            memo[cur] = dict()
            while len(minHeap) > 0:
                
                pop = heapq.heappop(minHeap)
                curPathWeight = pop[0]
                start = pop[1]
                
                if start not in memo[cur]:
                    memo[cur][start] = curPathWeight
                    if start in path:
                        for neighbor in path[start].keys():
                            heapq.heappush(minHeap, [curPathWeight + path[start][neighbor], neighbor])                            
            return
                
        path = dict()
        for e in edges:
            v1, v2, w = e[0], e[1], e[2]
            
            if v1 not in path:                
                path[v1] = dict()
                path[v1][v2] = w
            else:
                path[v1][v2] = w                
            
            if v2 not in path:                
                path[v2] = dict()
                path[v2][v1] = w
            else:
                path[v2][v1] = w
        
        memo = dict()
        for i in range(0, n):
            Dijkstra(n, path, i, memo)
        #print(memo)
                
        minCount = float('inf')
        res = -1
        for i in range(n - 1, -1, -1):
            count = 0
            for j in range(0, n):
                if i != j and j in memo[i] and memo[i][j] <= distanceThreshold:
                    count += 1                    
            if count < minCount:
                minCount = count
                res = i
        
        
        return res
    
    def findTheCity_DFS(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        '''
            find the cities with the smallest number of neighbors
            
            1. calculate all the min distance between all the cities -> O(n^2)
               then for each city, check how many neighbors there are in the dis smaller then distanceThreshold -> O(N ^ 2)               
               -> O(N^2) algorithm 
               
               -> wrong, no way to handle longer path with smaller weight sum
                (we'll need visited to avoid inner loop in dfs, but that also delete the ans of longer path with smaller sum)
        '''
        
        def getMinDis(i, j, path, memo, visited):
            
            if i in memo and j in memo[i]:
                return memo[i][j]
            
            visited.add(i)            
            # do dfs:
            nextSteps = path[i]
            minDis = float('inf')            
            for nextStep in nextSteps:
                if nextStep not in visited:                    
                    if nextStep == j:
                        minDis = min(minDis, path[i][j])
                    elif nextStep:
                        minDis = min(minDis, path[i][nextStep] + getMinDis(nextStep, j, path, memo, visited))                    
            
            visited.remove(i)
            if i not in memo:
                memo[i] = dict()            
            memo[i][j] = minDis
            
            if j not in memo:
                memo[j] = dict()            
            memo[j][i] = minDis            
            
            return memo[i][j]
                                
        path = dict()
        for e in edges:
            v1, v2, w = e[0], e[1], e[2]
            
            if v1 not in path:                
                path[v1] = dict()
                path[v1][v2] = w
            else:
                path[v1][v2] = w                
            
            if v2 not in path:                
                path[v2] = dict()
                path[v2][v1] = w
            else:
                path[v2][v1] = w
        
        memo = dict()                           
        for i in range(0, n):            
            for j in range(i + 1, n):                
                visited = set()
                getMinDis(i, j, path, memo, visited)
        
        print(memo)
        minCount = float('inf')
        res = -1
        for i in range(n - 1, -1, -1):
            count = 0
            for j in range(0, n):                
                if i != j and memo[i][j] <= distanceThreshold:
                    count += 1
            if count < minCount:
                minCount = count
                res = i                                                
        return res
                    
        
        
        
                    