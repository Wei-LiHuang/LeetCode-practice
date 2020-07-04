    def maxCoins(self, a: List[int]) -> int:
        
        def getNextSteps(a, curSeq, curCount, nextSteps):
            
            n = len(a)
            l = len(curSeq)        
            
            if l == 1:
            
                nextStr = ""
                nextCount = curCount + a[curSeq[0]]
                if nextStr in nextSteps:
                    nextSteps[nextStr][1] = max(nextSteps[nextStr][1], nextCount)
                else:
                    nextSteps[nextStr] = [[], nextCount]
            
            else:            
                for i in range(0, l):
                    nextCount, newSeq, nextStr = -1, None, ""
                    
                    if i == 0:
                        nextCount = curCount + 1 * a[curSeq[i]] * a[curSeq[i + 1]]
                        newSeq = curSeq[1 : l]
                        nextStr = str(newSeq)
                        
                    elif i == l - 1:
                        nextCount = curCount + a[curSeq[i - 1]] * a[curSeq[i]] * 1
                        newSeq = curSeq[0 : i]                        
                        nextStr = str(newSeq)                
                    else:
                        nextCount = curCount + a[curSeq[i - 1]] * a[curSeq[i]] * a[curSeq[i + 1]]
                        newSeq = curSeq[0 : i] + curSeq[i + 1 : l]
                        nextStr = str(newSeq)
                        
                    if nextStr in nextSteps:
                        nextSteps[nextStr][1] = max(nextSteps[nextStr][1], nextCount)
                    else:
                        nextSteps[nextStr] = [newSeq, nextCount]                      
            
            return
                
        
                
        n = len(a)

        indexSeq = []
        for i in range(0, n):
            indexSeq.append(i)
                
        # BFS
        stack = [[indexSeq, 0]]
        while len(stack) > 0:

            nextSteps = dict()
            curSize = len(stack)            
            for i in range(0, curSize):
                curNode = stack.pop()
                curSeq = curNode[0]
                curCount = curNode[1]                
                getNextSteps(a, curSeq, curCount, nextSteps)
            
            for node in nextSteps.values():
                stack.append(node)
                
            if len(stack) == 1:
                return stack[0][1]
                        
        return 0
