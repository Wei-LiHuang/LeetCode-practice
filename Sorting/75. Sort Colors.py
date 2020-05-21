# inplace sort -> heap sort

class Solution(object):
    
    def dripDown(self, a, i, end):
        
        l = 2 * i + 1
        r = 2 * i + 2
        
        target = i
        if l <= end and a[l] > a[i]:
            target = l

        if r <= end and a[r] > a[target]:
            target = r
            
        if i != target:
            a[i], a[target] = a[target], a[i]
            self.dripDown(a, target, end)
                                    
    
    def sortColors(self, a):
                
        #heapify:
        for i in range(len(a) - 1, -1, -1):
            self.dripDown(a, i, len(a) - 1)
        
        start, end = 0, len(a) - 1
        
        while end >= start:            
            a[start], a[end] = a[end], a[start]
            end -= 1
            self.dripDown(a, start, end)
        
        
        
