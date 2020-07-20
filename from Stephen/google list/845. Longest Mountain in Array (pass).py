#try onepass O(1) space
class Solution:
    
    def longestMountain(self, a: List[int]) -> int:
        
        res, n = 0, len(a)
        l = 0    
        while l < n - 2:            
            if a[l] >= a[l + 1]:
                l += 1 
                continue
            else:
                #start of the left mountain:
                peakIndex = l + 1
                while peakIndex < n - 1 and a[peakIndex] < a[peakIndex + 1]:
                    peakIndex += 1                    
                # now we get a possible peak index, find the end of the right side mountain:
                rightEndIndex = peakIndex
                while rightEndIndex < n - 1 and a[rightEndIndex] > a[rightEndIndex + 1]:
                    rightEndIndex += 1
                
                if rightEndIndex != peakIndex:
                    res = max(rightEndIndex - l + 1, res)                
                l = rightEndIndex
                                    
        return res
        
