# use mine heap, but need to be faster

# heapq with custom comparator:
# https://stackoverflow.com/questions/7803121/in-python-heapq-heapify-doesnt-take-cmp-or-key-functions-as-arguments-like-sor
# The traditional solution is to store (priority, task) tuples on the heap

class Solution:
    
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        
        if len(a) == 0 or len(b) == 0:
            return []
        
        heap = []        
        for i in range(0, len(a)):
            for j in range(0, len(b)):                
                heapq.heappush(heap, [a[i] + b[j], i, j])
                
        res = []
        for i in range(0, k):            
            res.append([a[heap[0][1]], b[heap[0][2]]])
            heapq.heappop(heap)
            if len(heap) == 0:
                break
            
        return res
                
                
