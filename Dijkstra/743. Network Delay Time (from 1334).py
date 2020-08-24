class Solution:
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:        
                        
        path = dict()
        for t in times:
            v1, v2, val = t[0] , t[1], t[2]
            if v1 not in path:                
                path[v1] = dict()
            path[v1][v2] = val
        
        received = dict()        
        minHeap = [[0, K]]
        while len(minHeap) > 0:            
            pop = heapq.heappop(minHeap)
            curNode, curTime = pop[1], pop[0]
            if curNode not in received:
                received[curNode] = curTime                                       
                if curNode in path:
                    for neighbor in path[curNode].keys():
                        heapq.heappush(minHeap, [path[curNode][neighbor] + curTime, neighbor])
            else:
                continue
                    
        receivedCount, maxTime = 0, -float('inf')        
        for node, time in received.items():
            receivedCount += 1
            maxTime = max(maxTime, time)
            
        if receivedCount < N:
            return -1
    
        return maxTime
                    
