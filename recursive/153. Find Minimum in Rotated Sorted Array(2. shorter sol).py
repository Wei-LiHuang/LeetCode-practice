class Solution:
    
    # find mid -> one is rotated (right < left), one is not rotated(left < right)
    # where will th min val be? in the seq which has the min among (l1, l2, r1, r2)
    # 601 2 345,  345 6 012, 123 4 560
    
    def findMin(self, a: List[int]) -> int:
        
        def bSearch(a, start, end):
            
            if start == end:
                return a[start]
                    
            mid = int((start + end) / 2)
            l1, r1, l2, r2 = start, mid, mid + 1, end
            
            if (a[l1] < a[l2] and a[l1] < a[r2]) or (a[r1] < a[l2] and a[r1] < a[r2]):
                return bSearch(a, l1, r1)
            else:
                return bSearch(a, l2, r2)
            
        
        return bSearch(a, 0, len(a) - 1)
                
