class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n, start, gasLeft = len(gas), 0, 0
        
        for i in range(0, n):            
            gasLeft += gas[i]            
            if gasLeft < cost[i]:
                gasLeft = 0
                start = i + 1
            else:
                gasLeft -= cost[i]
        
        if start == n:
            return -1
        
        for i in range(0, start):
            gasLeft += gas[i]
            if gasLeft < cost[i]:
                return -1
            else:
                gasLeft -= cost[i]
            
            
        return start
        
                
        
