# 1. sort, then three by three, switch the sec and third element -> O(N logN)
# 2. O(N)? switch the wrong element


class Solution:
    def wiggleSort(self, a: List[int]) -> None:
        
        needToBeBigger = False
        
        n = len(a)
        
        for i in range(0, n - 1):                                                            
            if needToBeBigger:
                if a[i] < a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                needToBeBigger = False
                                                
            else:
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                needToBeBigger = True    
                
                
        return a
            

        
