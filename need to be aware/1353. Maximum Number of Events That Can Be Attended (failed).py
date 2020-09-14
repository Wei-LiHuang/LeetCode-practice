class Solution:
    def maxEvents(self, a: List[List[int]]) -> int:
        
        def cmp(a2, a1):            
            #if same end date -> sort by starting date:
            if a1[1] == a2[1]:
                return a1[0] - a2[0]
            else:
                return a1[1] - a2[1]
        
        a.sort(reverse=1)
        print(a)
        h = []
        res, day = 0, 0
        
        while len(a) > 0 or len(h) > 0:
            
            if len(h) == 0: 
                day = a[-1][0]
                                
            # if any event start at/before day
            while len(a) > 0 and a[-1][0] <= day:
                heapq.heappush(h, a.pop()[1])
                
            heapq.heappop(h)
            res += 1
            day += 1
            
            # remove pass event
            while h and h[0] < day:
                heapq.heappop(h)
                
        return res
        
        
        
        
