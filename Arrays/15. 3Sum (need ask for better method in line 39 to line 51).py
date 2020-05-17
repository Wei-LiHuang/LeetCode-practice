# 1. use the 2-sum result:
#    2-sum is O(N), now for 3-sum, each element will need to perform 2-sum once -> O(N * N)

# how to define a self define struct? like for this, I want to sort but the res is build on the original index
# so I'll want to create a struct like:[i, nums[i]], and sort those pair byt the nums[i] value
# how to define a comparater like java?  sorted(subjects, operator.itemgetter(0), reverse=True)

# =======================================================================================================================
# trap: previous 2-sum guaranteed the ouput is unique. But here need to heanle set like this: 0:[0,0,0] or 0: [0,0,0,0]
# => can't use hash map, will have two val point to a same key value
# =======================================================================================================================

# 2. try to solve it using loop: 

# => need ask for better method in line 39 to line 51

class Solution(object):

    def threeSum(self, nums):        
                
        lst = sorted(nums)
        
        res = []
        for i in range(len(lst)):
            
            if i > 0 and lst[i] == lst[i - 1]:
                continue
                        
            v1 = lst[i]                     
            tgt = -lst[i]
            _dict = {}
            
            l = i + 1
            r = len(lst) - 1
                                    
            while (l < r):
                _sum = lst[l] + lst[r]
                if _sum == tgt:
                    _dict[lst[l]] = lst[r]
                    r -= 1
                    l += 1
                elif _sum < tgt:
                    l += 1              
                elif _sum > tgt:
                    r -= 1             
                          
            for v2, v3 in _dict.items():
                res.append([v1, v2, v3])
                          
        return res
        
