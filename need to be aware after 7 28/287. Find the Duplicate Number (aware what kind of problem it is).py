class Solution:
    
    def findDuplicate(self, a: List[int]) -> int:        
        
        if len(a) == 2:
            return a[0]
        
        slow = a[0]
        fast = a[0]
        while True:                                                 
            slow = a[slow]
            fast = a[a[fast]]
            if slow == fast:
                break       
            
        slow = a[0]
        while slow != fast:
            slow = a[slow]
            fast = a[fast]
                          
                
                
        return slow
