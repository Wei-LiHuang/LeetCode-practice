# rows and columns are sorted in ascending order:
# a[i][j] <= a[i + 1][j] for all i, j
# a[i][j] <= a[i][j + 1] for all i, j

# try 1:
# O(N^2 * log N^2), use min heap

# try 2:
# only put in min(n, k) elements into heap
# while heap pop out a element, heap push in the a[i][j + 1] element
# pop like this k times, get the answer
# O(l + k * log l), l = min(n, k)

class Solution:
    def kthSmallest(self, a: List[List[int]], k: int) -> int:
        
        n = len(a)        
        heap = []
        
        # l = min(n, k), O(l)
        for i in range(0, min(k, n)):
            heap.append([a[i][0], i, 0])
        
        # O(l)
        heapq.heapify(heap)
                
        # l = min(n, k), O(k * log l)
        for i in range(0, k - 1):
            pop = heapq.heappop(heap) # O(log l)
            if pop[2] < n - 1:
                heapq.heappush(heap, [a[pop[1]][pop[2]+ 1], pop[1], pop[2] + 1]) # O(log l)
            
        return heap[0][0]
                
