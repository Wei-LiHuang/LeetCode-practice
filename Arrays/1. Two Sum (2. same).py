class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        _dict = dict()
        for i in range(0, len(nums)):
            _dict[target - nums[i]] = i
        
        for i in range(0, len(nums)):
            if nums[i] in _dict and i != _dict[nums[i]]:
                return [i, _dict[nums[i]]]
        
        return -1
