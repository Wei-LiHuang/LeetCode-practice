# group can be strach
# consecutive same char more then three can be group:

# If a letter is not repeated in a word in the words list, the stretched word must contain either one such letter, or three or more such letters, but not two such letters.
# If a letter is repeated once (two same consecutive letters), the stretched word must contain two or more such letters.

class Solution:
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def countString(s: str):
            n, left, res = len(s), 0, []           
            for i in range(0, n):
                c = s[i]
                
                if i == n - 1 or s[i + 1] != c:
                    dis = i - left + 1
                    res.append([c, dis])
                    left = i + 1
                    
            return res
    
        sCount = countString(S)                                                                    
        
        res = 0
        for w in words:
            wCount = countString(w)
            compare = True
            
            if len(sCount) != len(wCount):                
                continue 
            
            for i in range(len(wCount) - 1, -1, -1):
                wPair = wCount[i]
                sPair = sCount[i]
                
                if wPair[0] != sPair[0]:
                    compare = False
                    break
                else:
                    if sPair[1] == 2 and wPair[1] != 2:
                        compare = False
                        break                        
                    elif sPair[1] < wPair[1]:
                        compare = False
                        break
            if compare:
                res += 1
        
        return res
            
