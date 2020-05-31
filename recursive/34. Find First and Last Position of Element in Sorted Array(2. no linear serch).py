class Solution:
    
    def searchRange(self, a: List[int], tgt: int) -> List[int]:        
    # if mid is tgt: left, right = mid
    # elif mid > tgt: left, right = mid - 1
    # elif mid < tgt: left = mid + 1, right
        n = len(a)
        left, right = 0, n - 1
        while(left < right):
            mid = (left + right) // 2
            if a[mid] == tgt:
                right = mid            
            elif a[mid] > tgt:
                right = mid - 1
            elif a[mid] < tgt:
                left = mid + 1
                
        if left == n or a[left] != tgt:
            return [-1, -1]    
        
        r1 = left
        left, right = 0, n - 1
    # if mid is tgt: left = mid, right
    # elif mid > tgt: left, right = mid - 1
    # elif mid < tgt: left = mid + 1, right
        while(left < right):
            mid = (left + right) // 2 + 1
            if a[mid] == tgt:
                left = mid
            elif a[mid] > tgt:
                right = mid - 1
            elif a[mid] < tgt:
                left = mid + 1        

        return [r1, left]
