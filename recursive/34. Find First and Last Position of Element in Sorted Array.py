class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def res(a, start, end, tgt):
            
            if start == end :
                if a[start] == tgt:
                    return start
                else:
                    return -1
                
            elif start == end - 1:
                if a[start] == tgt:
                    return start
                elif a[end] == tgt:
                    return end
                else:
                    return -1
            else:
                mid = int((start + end) / 2)
                
                if tgt == a[mid]:
                    return mid
                elif tgt < a[mid]:
                    return res(a, start, mid, tgt)
                elif tgt > a[mid]:
                    return res(a, mid, end, tgt)
        
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        index =  res(nums, 0, n - 1, target)
                    
        if index == -1:
            return [-1, -1]
        else:
            l, r = index, index
            while l > 0 and nums[l - 1] == nums[index]:
                l -= 1
            while r < n - 1 and nums[r + 1] == nums[index]:
                r += 1
            
            return [l, r]
