class Solution:
    
    def findDuplicates(self, a: List[int]) -> List[int]:
        
        '''
            hint1: 1 ≤ a[i] ≤ n 
            hint2: at most appear twice
        '''                
        res = []
        for i in range(0, len(a)):
            val = a[i]
            if val < 0:
                val *= -1            
            index = val - 1           
            if a[index] < 0:
                res.append(val)
            else:
                a[index] *= -1
                #print(a)                
        return res
