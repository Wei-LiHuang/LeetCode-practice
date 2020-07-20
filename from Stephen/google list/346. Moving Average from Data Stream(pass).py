class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self._sum = 0
        self.k = size        
                
    def next(self, val: int) -> float:                
        if len(self.q) < self.k:                                
            self.q.append(val)
            self._sum += val                                       
        else:
            popLeft = self.q.popleft()
            self._sum -= popLeft
            self.q.append(val)
            self._sum += val
        
        return self._sum/len(self.q)                                    
        
