class Solution:
    
    def canJump(self, a: List[int]) -> bool:
        
        start, rightMost, n = 0, 0, len(a)
        
        for i in range(0, n):
            
            if i <= rightMost:
                rightMost = max(rightMost, i + a[i])
                
            if rightMost == i and rightMost != n - 1:
                return False
        
        
        return True
        

            
