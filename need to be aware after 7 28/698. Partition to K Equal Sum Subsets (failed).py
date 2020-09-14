class Solution:
    
    def canPartitionKSubsets(self, a: List[int], k: int) -> bool:                
        '''
            k sub arr whose sum is equal -> each sub arr sum should be (total // k)
        '''        
        def dfs(a, used, index, tgt, curSum, groupCount):
            
            if curSum == tgt:  
                groupCount -= 1
                if groupCount == 0:                    
                    return True
                else:
                    return dfs(a, used, 0, tgt, 0, groupCount)
            
            for i in range(index, len(a)):                                
                if i not in used:                    
                    if a[i] > tgt:
                        return False                    
                    elif curSum + a[i] <= tgt:
                        used.add(i)                                        
                        if dfs(a, used, i + 1, tgt, curSum + a[i], groupCount):
                            return True     
                        used.remove(i)
            
            return False
        
        tgt =  sum(a) // k                
        res = dfs(a, set(), 0, tgt, 0, k)
        
        return res      
