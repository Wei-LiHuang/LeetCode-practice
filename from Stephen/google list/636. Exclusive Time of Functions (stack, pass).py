class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        '''
            n = 2
            logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]            
            0: start at 0,
                1 start at 2                
                1 end at 5
            0: end at 6                                                    
        '''
        def readLog(log):
            index, action, time = "", "", ""            
            isAction, isTime = False, False
            for c in log:
                if isAction == False and isTime == False:
                    if c == ':':
                        isAction = True
                    else:
                        index += c                                                            
                elif isAction and isTime == False:
                    if c == ':':
                        isTime = True
                    else:
                        action += c
                elif isAction and isTime:
                    time += c
                    
            return [int(index), action, int(time)]
            
        res = [0] * n
        l = len(logs)
        stack = []        
        for i in range(0, l):            
            log = readLog(logs[i])
            index, action, time = log[0], log[1], log[2]
            if action == "start":
                stack.append([index, time, 0])                        
            else:
                popped = stack.pop()
                excTime = time - popped[1] + 1
                if len(stack) > 0:
                    stack[-1][2] += excTime                
                res[popped[0]] += excTime - popped[2]
                
                
                
        return res
            
        
