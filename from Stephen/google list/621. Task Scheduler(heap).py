class Solution:
    
    def leastInterval(self, a: List[str], n: int) -> int:
        
        '''
            n: cool down time for two same task
            return the least number of time slot needed for the given tasks
            ================================================================
            we dont want same tasks -> try to avoid it
            start from the most popular task, and insert the second popular ones
                -> use heap to get the most popular one?
                -> poll: logN, push: logN, do N times -> O(NlogN)
                
            how could we do better? O(N), because the heap size is always 26, so poll and push might be O(1)
        '''
        
        def insertToSchedule(sch, h, idle, n):
            
            if idle > n:
                #print(sch)
                return
            
            if len(h) > 0:
                pop = heapq.heappop(h)                
                sch.append(pop[1])                    
                insertToSchedule(sch, h, idle + 1, n)                    
                pop[0] += 1
                if pop[0] < 0:
                    heapq.heappush(h, pop)                
            else:
                sch.append(None)
                insertToSchedule(sch, h, idle + 1, n)
                                
            return
                                                                                            
        d = dict()
        for c in a:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        h = []
        for key, val in d.items():
            h.append([-val, key])
                                
        heapq.heapify(h)
                
        schedule = []
        while len(h) > 0:
            insertToSchedule(schedule, h, 0, n)
            
        while schedule[-1] is None:
            schedule.pop()
            
        return len(schedule)
