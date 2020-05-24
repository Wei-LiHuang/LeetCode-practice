# group can be strach
# consecutive same char more then three can be group:

# If a letter is not repeated in a word in the words list, the stretched word must contain either one such letter, or three or more such letters, but not two such letters.
# If a letter is repeated once (two same consecutive letters), the stretched word must contain two or more such letters.


class Solution:
    
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def countToStack(w: str):
            n = len(w)
            stack = []        
            start = 0

            for i in range(0, n):                        
                if i == n - 1 or w[i] != w[i + 1]:
                    stack.append([w[start], i - start + 1])
                    start = i + 1
            return stack
                    
            
        if len(s) == 0:
            return 0
        
        sStack = countToStack(s)            
        sLen = len(sStack)
        
        res = 0
        for w in words:
            wStack = countToStack(w)
            wLen = len(wStack)
            if sLen != wLen:
                continue
            else:                
                parse = True
                for i in range(wLen - 1, -1, -1):
                    sPair = sStack[i]
                    wPair = wStack[i]
                    if sPair[0] != wPair[0]:
                        parse = False
                        break
                    else:
                        if sPair[1] == 2 and wPair[1] != 2:
                            parse = False
                            break
                        elif sPair[1] < wPair[1]:
                            parse = False
                            break
                if parse:
                    res += 1
                                                                                        
        return res
            
                
            
