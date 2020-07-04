class Solution:
    
    def countOfAtoms(self, s: str) -> str:
        
        def isUpperCase(c):
            return ord(c) >= ord('A') and ord(c) <= ord('Z')
        
        def isLowerCase(c):
            return ord(c) >= ord('a') and ord(c) <= ord('z')
        
        def isNum(c):
            return ord(c) >= ord('0') and ord(c) <= ord('9')
                
        
        def rec(s, l, r, pair):
            
            _dict = dict()
            stack = []            
            i = l
            while i <= r:                
                if s[i] == '(':                                        
                    midDict = rec(s, i + 1, pair[i] - 1, pair)
                    # move to "pos )" + 1
                    i = pair[i] + 1
                    
                    multiply = 1
                    if i <= r and isNum(s[i]):
                        numStr = ""                        
                        while i <= r and isNum(s[i]):
                            numStr += s[i]
                            i += 1
                            
                        #print(numStr)    
                        multiply = int(numStr)
                                                                                                                        
                    for key, val in midDict.items():
                        if key in _dict:
                            _dict[key] += (val * multiply)
                        else:
                            _dict[key] = val * multiply
                
                elif isUpperCase(s[i]):
                    elementStr = s[i]
                    i += 1
                    
                    if i == r + 1 or isUpperCase(s[i]) or s[i] == '(':
                        if elementStr not in _dict:
                            _dict[elementStr] = 1
                        else:
                            _dict[elementStr] += 1                            
                    else:
                        if isLowerCase(s[i]):
                            while i <= r and isLowerCase(s[i]):
                                elementStr += s[i]
                                i += 1                        
                            #print(elementStr)                    
                                                
                        multiply = 1
                        if i <= r and isNum(s[i]):
                            numStr = ""
                            while i <= r and isNum(s[i]):
                                numStr += s[i]
                                i += 1
                            multiply = int(numStr)
                            #print(numStr)
                        if elementStr not in _dict:
                            _dict[elementStr] = multiply
                        else:
                            _dict[elementStr] += multiply                          
                        
            
            #print(_dict)
            return _dict

                                                                                           
        n, i = len(s), 0
        
        pair = dict()
        stack = []
        for i in range(0, n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                pair[stack.pop()] = i
                
        _dict = rec(s, 0, n - 1, pair)

        #sort
        elementList = []
        for key in _dict.keys():
            elementList.append(key)
            
        elementList.sort()
        
        res = ""
        for element in elementList:
            res += element
            if _dict[element] != 1:
                res += str(_dict[element])
        
            
        return res
