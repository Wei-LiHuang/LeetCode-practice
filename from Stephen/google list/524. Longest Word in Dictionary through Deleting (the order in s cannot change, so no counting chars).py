class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        '''
            1. turn each words in d as counting chars, 
                if any char in the word exceed the limit of s, remove it from the d                
                O(len of d) -> wrong, we can't change the order of the word char
                
                -> check s and w in d one by one -> two pointers
                                
            2. try to remove one char in s, and see if the new s in the d or not                                                
                O(len s !)
        '''                        
        def cmp(w1, w2):
            if w1 == w2:
                return 0
            if len(w1) != len(w2):
                return len(w2) - len(w1)
            
            i1, i2 = 0, 0
            while w1[i1] == w2[i2]:
                i1 += 1
                i2 += 1
                
            return ord(w1[i1]) - ord(w2[i2])                                                                
        d = sorted(d, key = cmp_to_key(cmp))
        #print(d)
        
        if len(s) == 0:
            return ""
                
        for w in d:            
            i = 0
            found = True
            for j in range(0, len(w)):
                
                c = w[j]                
                while i < len(s) and s[i] != c:                    
                    i += 1
                                                
                if i >= len(s) and j <= len(w) - 1:
                    found = False
                    break
                
                i += 1
                                    
            if found:
                return w         
            
        return ""
