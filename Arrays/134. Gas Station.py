# is this solution bad? 
# Although I used two loop, the index "start" will only traverse the list once

class Solution(object):
    
    def canCompleteCircuit(self, gas, cost):
        
        l = 0
        n = len(gas)                    
        going =True
        
        while going:                        
            cur = 0
            start = l            
            for r in range(start, start + n):                                                
                end = r % n
                cur = cur + gas[end] - cost[end]                            
                if cur >= 0:
                    end += 1
                    if end % n == l:
                        return l                    
                else:                    
                    l = r + 1                        
                    cur = 0
                    break                           
            if l >= n:
                break     
                
        return -1        
        
        #test use the max diff station: failed
        #if sum(gas) < sum(cost):
            #return -1
        
        #diff = []
        #maxDiffStation = -1
        #maxDiff = 0
        #for i in range(0, n):
            #diff.append(gas[i] - cost[i])
            #if diff[i] > maxDiff:
                #maxDiff = diff[i]
                #maxDiffStation = i
                
        #return maxDiffStation                            
    
