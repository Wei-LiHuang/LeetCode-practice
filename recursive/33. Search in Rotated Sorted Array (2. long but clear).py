# mid > tgt: look into left side
# mid < tgt: look into right side
# mid == tgt: return mid index

#just perform binary search. At worst search twice. still O(lgN) -> X

# when we got a mid, only one side between left and right will be rotated
# for the one is not rotated: check min and max, if the target is in this side -> binary search
# for the rotated side: repeat the previous step


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(a: List[int], start: int, end: int, tgt: int):
            if start == end:
                if a[start] == tgt:
                    return start
                else:
                    return -1
            elif start == (end - 1):
                if a[start] == tgt:
                    return start
                elif a[end] == tgt:
                    return end
                else:
                    return -1
            else:
                midIndex = int((start + end) / 2)
                if a[midIndex] == tgt:
                    return midIndex
                elif tgt > a[midIndex]:
                    # go right:
                    return binarySearch(a, midIndex + 1, end, tgt)
                elif tgt < a[midIndex]:
                    # go left:
                    return binarySearch(a, start, midIndex - 1, tgt)
        
        def binarySearchInRotatedArray(a: List[int], start: int, end: int, tgt: int):
            
            if start == end or start == (end - 1):
                return binarySearch(a, start, end, tgt)
            else:
                midIndex = int((start + end) / 2)
                if a[midIndex] == tgt:
                    return midIndex
                
                leftSideStart, leftSideEnd = start, midIndex
                rightSideStart, rightSideEnd = midIndex + 1, end
                                                
                if a[leftSideEnd] < a[leftSideStart]:
                    #left is the rotated side:
                    if tgt >= a[rightSideStart] and tgt <= a[rightSideEnd]:
                        return binarySearch(a, rightSideStart, rightSideEnd, tgt)
                    else:
                        return binarySearchInRotatedArray(a, leftSideStart, leftSideEnd, tgt)
                else:
                    #right is the rotated side:
                    if tgt >= a[leftSideStart] and tgt <= a[leftSideEnd]:
                        return binarySearch(a, leftSideStart, leftSideEnd, tgt)
                    else:
                        return binarySearchInRotatedArray(a, rightSideStart, rightSideEnd, tgt)                    
                    
                
        start, end = 0, len(nums)
        
        if end == 0:
            return -1
        
        return binarySearchInRotatedArray(nums, 0, len(nums) - 1, target)
