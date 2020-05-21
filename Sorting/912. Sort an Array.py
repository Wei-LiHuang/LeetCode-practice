# sort: bubble, select, merge, quick, heap, radix, bucket...
# knowing the range => can use linear sort

# today: implement merge sort => slow

# quick sort: 
# if we need to find median as pivot: use two heap => O(lgN)
# for now, we just use the first element: will have endless loop
# pivot need random: random.choice(nums)

#heap sort:
# view the original array as a tree, calls heapify -> heap
# remove the max/min element from the heap, put into the max/min pos in the sorted array
# drip down the swapped element
# repeat the process

class Solution(object):
    
    # merge:
    def merge(self, l1, l2):         
        n1, n2 = len(l1), len(l2)
        i1, i2 = 0, 0
        
        res = []
        while i1 < n1:        
            v1 = l1[i1]                                    
            if i2 < n2:
                v2 = l2[i2]
                if v2 < v1:
                    res.append(v2)
                    i2 += 1
                    continue
            
            res.append(v1)
            i1 += 1
        
        while i2 < n2:
            res.append(l2[i2])
            i2 += 1
        
        return res        
    
    def mergeSort(self, a):
        
        # break into many lists: O(N)
        lst = []
        for i in a:
            lst.append([i])
        
        # merge two by two:
        m = []
        i = 0
        while len(lst) != 1:
            if i == len(lst) - 1:
                m.append(lst[i])
                i += 1                
            elif i < len(lst) - 1:
                m.append(self.merge(lst[i], lst[i + 1]))
                i += 2
            elif i >= len(lst):
                lst = m
                m = []
                i = 0
                
        return lst[0]
      
    #quick:
    def _quicksort(self, a):
        
        if len(a) <= 1:
            return a
        
        pivot = random.choice(a)
        small = []
        big = []
        equal = []
        
        for i in a:
            if i < pivot:
                small.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                big.append(i)
                
        return self._quicksort(small) + equal + self._quicksort(big)
                                
    def quickSort(self, a):
        return self._quicksort(a)
        
    #heap:2,8,5,3,9,1 => 9,8,5,3,2,1 => 1,8,5,3,2 | 9....        
    def dripDown(self, a, i, end):
        left = i * 2 + 1
        right = i * 2 + 2

        target = i
        if left <= end and a[left] > a[i]:
            target = left
        if right <= end and a[right] > a[target]:
            target = right
            
        if target != i:
            a[i], a[target] = a[target], a[i]
            self.dripDown(a, target, end)
                                                
    def heapSort(self, a):      
        
        for i in range(len(a) - 1, -1, -1):                
            self.dripDown(a, i, len(a) - 1)
            
        start, end = 0, len(a) - 1    
            
        while end >= start:            
            a[start], a[end] = a[end], a[start]
            end -= 1
            self.dripDown(a, start, end)
        
        return a                                                
        
                        
    def sortArray(self, a):
        #return self.mergeSort(a)
        #return self.quickSort(a)
        return self.heapSort(a)
