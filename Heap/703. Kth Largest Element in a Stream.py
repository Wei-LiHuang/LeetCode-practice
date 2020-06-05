class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

                                                
    def add(self, val: int) -> int:
        
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]
            
        kthMax = self.minHeap[0]
        
        if val > kthMax:
            heapq.heappush(self.minHeap, val)
            heapq.heappop(self.minHeap)
            return self.minHeap[0]
            
        elif val == kthMax:        
            return kthMax
        
        elif val < kthMax:
            return kthMax
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
