# mid > tgt: look into left side
# mid < tgt: look into right side
# mid == tgt: return mid index

#just perform binary search. At worst search twice. still O(lgN)


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        

        def rec(a, l, r, tgt):
                        
            if l == r:
                if tgt == a[l]:
                    return l
                else:
                    return -1
                
            elif r - 1 == l:
                if tgt == a[l]:
                    return l
                elif tgt == a[r]:
                    return r
                else:
                    return -1
                
            else:            
                midIndex = int((r + l) / 2)
                if a[midIndex] == tgt:
                    return midIndex                
                f1 = rec(a, l, midIndex, tgt) 
                
                if f1 != -1:
                    return f1
                else:
                    return rec(a, midIndex, r, tgt)
                
                                                                     
        start, end = 0, len(nums) - 1
        
        if end < 0:
            return -1
        
        return rec(nums, start, end, target)
        
