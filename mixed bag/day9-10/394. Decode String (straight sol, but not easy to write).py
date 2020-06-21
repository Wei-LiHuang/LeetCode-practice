class Solution:
    def decodeString(self, s: str) -> str:
        
        def rec(s, l, r, pair):
            
            res = ""
            i = l

            num = 0
            while i < r:
                curChar = s[i]
                
                if curChar.isnumeric():
                    j = i
                    numStr = ""
                    while s[j].isnumeric():
                        numStr += s[j]
                        j += 1
                    
                    i = j
                    num = int(numStr)
                                        
                elif s[i] == '[':                    
                    subStr = rec(s, i + 1, pair[i], pair)                    
                    for j in range(0, num):
                        res += subStr
                    i = pair[i] + 1
                
                else:
                    res += s[i]
                    i += 1
            
            return res
            
                        
        n = len(s)        
        stack, pair = [], dict()
        
        for i in range(0, n):
            if s[i] == '[':
                stack.append(i)
            elif s[i] == ']':
                pair[stack.pop()] = i
                        
        return rec(s, 0, n, pair)
                
                
