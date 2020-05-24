# how to check is Alphanumeric in python?

class Solution:
    
    def isAlphanumeric (self, c):
        
        
        b1 = ord(c) <= ord('z') and ord(c) >= ord('a')
        b2 = ord(c) <= ord('9') and ord(c) >= ord('0')
        
        return b1 or b2
        
    
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        n = len(s)
        l = 0
        r = n - 1
        
        while l < r:
            
            left = s[l]
            right = s[r]
            
            #if not self.isAlphanumeric(s[l]):
            if not s[l].isalnum():
                l += 1
                continue
            #if not self.isAlphanumeric(s[r]):
            if not s[r].isalnum():
                r -= 1
                continue
                                
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
            
        
        return True
