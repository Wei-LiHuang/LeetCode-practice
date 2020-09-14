class Solution:
    def shortestDistance(self, a: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        '''
            shortestDistance -> BFS        
        '''
        
        def findNextStop(a, r, c):
            
            m, n = len(a), len(a[0])
                                    
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            nextSteps = []
            for d in directions:                                
                nr, nc = r, c    
                while nr + d[0] >= 0 and nr + d[0] < m and nc + d[1] >= 0 and nc + d[1] < n and a[nr + d[0]][nc + d[1]] != 1:
                    nr += d[0]
                    nc += d[1]                                
                nextSteps.append([nr, nc])                                        
                
            return nextSteps
                            
        m, n = len(a), len(a[0])        
        
        q, dis = collections.deque(), dict()
        
        dis[start[0] * n + start[1]] = 0        
        q.append(start)                                
        
        while len(q) > 0:
            curSize = len(q)

            for i in range(0, curSize):                
                pop = q.pop()
                r, c = pop[0], pop[1]                                                                
                index = r * n + c                                
                
                #if r == destination[0] and c == destination[1]:
                    #return dis[index]
                    #print(dis[index])                    
                '''                                    
                    this is where my mistake is.
                    BFS did promise the "shortest turn" to reach the tgt
                    but it did not promise the "shortest distance"
                    so if I return when I first reach the tgt, it might be a wrong answer
                '''                                                                    
                nextSteps = findNextStop(a, r, c)
                for ns in nextSteps:
                    index2 = ns[0] * n + ns[1]
                    newDis = dis[index] + abs(ns[0] - r) + abs(ns[1] - c)                    
                    if index2 not in dis or newDis < dis[index2]:                    
                        dis[index2] = dis[index] + abs(ns[0] - r) + abs(ns[1] - c)
                        q.appendleft(ns)
        
        tgt = destination[0] * n + destination[1]
        if tgt not in dis:        
            return -1
        else:
            return dis[tgt]
        
