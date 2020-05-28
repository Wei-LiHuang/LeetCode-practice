# how to check is Alphanumeric in python? isalnum()

class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        n = len(s)
        left, right= 0, n - 1
        
        while left < right:
            l = s[left]
            r = s[right]
            
            if not l.isalnum():
                left += 1
                continue
            if not r.isalnum():
                right -= 1
                continue
                
            if l != r:
                return False
            else:
                left += 1
                right -= 1
    
        return True
        
        
        
