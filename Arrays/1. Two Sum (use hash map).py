class Solution(object):
    def twoSum(self, nums, target):
        _dict = dict()
        
        for i in range(len(nums)):            
            _dict[target - nums[i]] = i
            
        res = [];
        
        for i in range(len(nums)):
            if nums[i] in _dict and _dict[nums[i]] != i:
                res.append(i)
                res.append(_dict[nums[i]])
                break
        return res       
        
