# you are guaranteed that there will always be only one unique minimum window in S, it not, return ""
# T: ABC
# S: ADOBECODEBANC
# A, AD, ADO, ADOB, ADOBE, ADOBEC(contains all T, update answer)
# ADOBECO, ADOBECOD, ADOBECODE, ADOBECODEB(B is in T, can we update left index? => no)
# ADOBECODEBA(A is in T, can we update left index? => yes ... move left index one by one) -> CODEBA
# CODEBAN, CODEBANC (C is in T, update left index)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
                                
        # if s[start] is a target:
            # start to end satisfied: record the length, move left to another target(find next min substring)
                # satisfied: diff == 0 
            # start to end not satisfied: start remains the same, move right until meet the requirement (loop)
                # satisfied: diff != 0  
        
        # if s[start] is not a target:
            # move start until it is a target
            
        # 1. setup target map:
        diff = 0
        target = {}
        for c in t:
            val = target.get(c, 0)
            target[c] = val + 1
            diff += 1
            
        # 2. setup current map:
        current = {}
        n = len(s)
        start, end, parsed, minL, minStr = 0, 0, -1, n + 1, ""
        while start < n: #O(N)
            if s[start] not in target:#OBEC, BEC, ECODEB, ODEBA, DEBA, EBA
                start += 1
                if end < start:
                    end = start
                continue
            else:
                startChar = s[start]
                if start > parsed:
                    diff -= 1
                    parsed = start
                    val = current.get(startChar, 0)
                    current[startChar] = val + 1
                
                #check for moving start for redundant taget start:
                if startChar in target and startChar in current and current[startChar] > target[startChar]:
                    current[startChar] -= 1
                    start += 1
                    continue
                                                            
                if diff == 0:
                    curLen = end - start + 1
                    if curLen < minL:
                        minL = curLen
                        minStr = s[start:end + 1]
                    # move start to another target:
                    diff += 1
                    current[startChar] -= 1
                    if current[startChar] == 0:
                        current.pop(startChar)                        
                    start += 1 #1,5: DOBEC, ODEBA
                    if end < start:
                        end = start
                    continue    
                    
                else: # diff != 0, move end index
                    endChar = s[end] #0,0:A -> 0,1 :AB ->...->0,5:ADOBEC, CODEB, CODEBA, BA, BANC
                    if endChar in target and end > parsed:
                        val = current.get(endChar, 0)
                        if val < target[endChar]:
                            diff -= 1
                        elif val >= target[endChar] and startChar == endChar:
                            current[startChar] = val - 1
                            start += 1
                                                        
                        current[endChar] = current.get(endChar, 0) + 1
                        parsed = end
                        if diff == 0: #CODEBA
                            continue
                    
                    
                    end += 1 #BECO, BECOD, BECODE, ECODEB, BAN
                    if end == n:
                        break

                                        
        return minStr
       
