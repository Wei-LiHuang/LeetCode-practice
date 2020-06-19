# use heap, but need to be faster

class Solution:
    
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
                
        def heapifyBotUp(a, index):                       
            parent = (index - 1) // 2                        
            if parent >= 0:
                sumParent = sum(a[parent])
                sumChild = sum(a[index])            
                if sumChild < sumParent:
                    a[parent], a[index] = a[index], a[parent]
                    heapifyBotUp(a, parent)
        
        def heapifyTopDown(a, index, end):
            left = 2 * index + 1
            right = 2 * index + 2
            
            _max = index            
            sumParent = sum(a[index])
            sumMax = sumParent
            
            if left < end:                
                sumLeft = sum(a[left])
                if sumLeft < sumParent:
                    _max = left
                    sumMax = sumLeft
                    
            if right < end:
                sumRight = sum(a[right])
                if sumRight < sumMax:
                    _max = right
            
            if _max != index:
                a[index], a[_max] = a[_max], a[index]
                heapifyTopDown(a, _max, end)
                
        heap = []        
        for i in range(0, len(a)):
            for j in range(0, len(b)):                
                heap.append([a[i], b[j]])
                heapifyBotUp(heap, len(heap) - 1)
                                
        res = []
        end = len(heap)
        for i in range(0, len(heap)):
            res.append(heap[0])
            if len(res) == k:
                break                        
            heap[0], heap[end - 1] = heap[end - 1], heap[0]
            heapifyTopDown(heap, 0, end - 1)
            end -= 1
            
        return res
            
        
            
