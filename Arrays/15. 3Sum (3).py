# 1. use the 2-sum result:
#    2-sum is O(N), now for 3-sum, each element will need to perform 2-sum once -> O(N * N)

# how to define a self define struct? like for this, I want to sort but the res is build on the original index
# so I'll want to create a struct like:[i, nums[i]], and sort those pair byt the nums[i] value
# how to define a comparater like java?  sorted(subjects, operator.itemgetter(0), reverse=True)

# =======================================================================================================================
# trap: previous 2-sum guaranteed the ouput is unique. But here need to heanle set like this: 0:[0,0,0] or 0: [0,0,0,0]
# => can't use hash map, will have two val point to a same key value
# =======================================================================================================================


class Solution(object):

    def threeSum(self, a):        
        
        a.sort()
        res, n = [], len(a)
                
        for i in range(0, n):            
            
            if a[i] > 0:
                break
                
            if i > 0 and a[i] == a[i - 1]:
                continue
                    
            tgt, left, right = -a[i], i + 1, n - 1            
            while left < right:                
                _sum = a[left] + a[right]
                if _sum < tgt or (left > i + 1 and a[left] == a[left - 1]):
                    left += 1
                elif _sum > tgt or (right < n - 1 and a[right] == a[right + 1]):
                    right -= 1
                elif _sum == tgt:
                    res.append([a[i], a[left], a[right]])
                    left += 1
                    right -= 1
                                                                      
        return res
        
        
