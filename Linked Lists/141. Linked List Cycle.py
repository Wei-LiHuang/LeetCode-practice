#141. Linked List Cycle

class Solution(object):
    
    def check(self, f, s):
        if f is None or f.next is None:
            return 1        
        if f is s:
            return 2                
        return 3
    
    def hasCycle(self, head):
                
        s = head;
        
        if head is None:
            return False
        
        if head.next is None:
            return False
        else:
            f = head.next
                        

        while f is not s:            
            c = self.check(f,s)
            if c == 1:
                return False
            
            if c == 2:
                return True
            
            if c == 3:
                f = f.next.next
                s = s.next
                    
        return True
