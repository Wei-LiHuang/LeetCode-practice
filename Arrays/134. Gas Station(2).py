class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        # find a start can reach n - 1
        gasLeft = 0
        n = len(gas)        
        
        start = -1        
        i = 0
        while i < n:
            cur = i                                
            while cur <= n - 1:
                gasLeft += gas[cur]
                gasLeft -= cost[cur]
                if gasLeft < 0:
                    gasLeft = 0
                    i = cur + 1
                    break
                else:
                    cur += 1             
            if cur == n:
                start = i
                break
                
        if start == -1:
            return -1
        
        # check 0 to i with current gasLeft:
        for j in range(0, i):
            gasLeft += gas[j]
            gasLeft -= cost[j]
            if gasLeft < 0:
                return -1
        
        return start
            
            
            
