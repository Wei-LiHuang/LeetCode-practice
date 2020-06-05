class Solution:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        mH = []
        heapq.heapify(mH)
        
        disToPoint = dict()
        for p in points:
            d = p[0] * p[0] + p[1] * p[1]
            
            if d in disToPoint:
                disToPoint[d].append(p)
            else:    
                disToPoint[d] = [p]
                
            heapq.heappush(mH, d)
            
        res = []
        while len(res) < K:
            dis = heapq.heappop(mH)
            res.extend(disToPoint[dis])
        
        return res
            
        
