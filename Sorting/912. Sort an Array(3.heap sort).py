class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def dripDown(a, i, end):            

            left, right = 2 * i + 1, 2 * i + 2                                 

            target = i
            if left <= end and a[i] < a[left]:
                target = left                    

            if right <= end and a[target] < a[right]:
                target = right

            if target != i:
                a[i], a[target] = a[target], a[i]            
                dripDown(a, target, end)
            
        #heap:2,8,5,3,9,1 => 9,8,5,3,2,1 => 1,8,5,3,2 | 9....                        
        def heapSort(a):
            
            n = len(a)        
            
            for i in range(n - 1, -1, -1):                
                dripDown(a, i, n - 1)
                            
            end = n - 1            
            while end >= 0:            
                a[0], a[end] = a[end], a[0]
                end -= 1
                dripDown(a, 0, end)
            return a
        
        return heapSort(nums)
                

                    
