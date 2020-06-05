# heapq : [small -> big]
# use maxHeap & minHeap
# because heapQ is small to big, max heap need to be reverse: every element in maxHeap *= -1
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        
        self.minHeap = []
        heapq.heapify(self.minHeap)
                
    def addNum(self, num: int) -> None:
        
        n1, n2 = len(self.maxHeap), len(self.minHeap)
        
        if n2 == 0:
            heapq.heappush(self.minHeap, num)
            return
        else:        
            rightVal = self.minHeap[0]

            if num < rightVal:
                heapq.heappush(self.maxHeap, -num)
                n1 += 1
                if n1 == n2 + 2:
                    pop = -heapq.heappop(self.maxHeap)
                    heapq.heappush(self.minHeap, pop)              
            else:
                heapq.heappush(self.minHeap, num)
                n2 += 1
                if n2 == n1 + 2:
                    pop = heapq.heappop(self.minHeap)
                    heapq.heappush(self.maxHeap, -pop)
                        
    def findMedian(self) -> float:        
        n1, n2 = len(self.maxHeap), len(self.minHeap)
        
        if n2 == 0:
            return 0.0
        else:                                    
            if n1 == n2:
                return (-self.maxHeap[0] + self.minHeap[0]) / 2
            elif n1 > n2:
                return -1 * self.maxHeap[0]
            else:
                return self.minHeap[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
