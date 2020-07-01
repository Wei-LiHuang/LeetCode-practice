# use min heap, but need to be faster -> use pop to find the next heap element

# heapq with custom comparator:
# https://stackoverflow.com/questions/7803121/in-python-heapq-heapify-doesnt-take-cmp-or-key-functions-as-arguments-like-sor
# The traditional solution is to store (priority, task) tuples on the heap

class Solution:
    
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        
        if len(a) == 0 or len(b) == 0:
            return []
        
        h = []
        for i in range(0, len(b)):
            heapq.heappush(h, [a[0] +  b[i], [0, i]])

        res = []
        for i in range(0, k):
            pop = heapq.heappop(h)
            aIndex = pop[1][0]
            bIndex = pop[1][1]
                        
            res.append([a[aIndex], b[bIndex]])
            
            if aIndex < len(a) - 1:
                heapq.heappush(h, [a[aIndex + 1] +  b[bIndex], [aIndex + 1, bIndex]])
                
            if len(h) == 0:
                break
        
        return res
            
