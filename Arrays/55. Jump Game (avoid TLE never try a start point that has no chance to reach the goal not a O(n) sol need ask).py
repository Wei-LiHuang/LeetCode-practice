# avoid TLE: never try a start point that has no chance to reach the goal
# not a O(n) sol, need ask

class Solution(object):
    
    def canJump(self, nums):
        lst = []
        
        for i in range(0, len(nums)):
            lst.append(False)
                
        leftMost = 0        
        for i in range(len(nums) - 1, -1, -1):
            
            if i == len(nums) - 1:
                lst[i] = True
                leftMost = i
                continue
                
            for j in range(leftMost, nums[i] + i + 1):
                lst[i] = lst[j] or lst[i]
                if lst[i]:
                    break;
            
                
        return lst[0]
