#try onepass O(1) space
class Solution:
    
    def longestMountain(self, a: List[int]) -> int:
        
        n = len(a)
        if n <= 2:
            return 0    
        #return 0 if no mountain:
        left, mid, right, res = 0, 0, 0, 0
        
        # 2 1 4 7 3 2 5
        # left = 0, mid = 0. right = 0
        # 1. if a[left + 1] > a[left]: can be a mid, so mid and right move to left + 1
        #    else: a[left] >= a[left + 1]: left move to left + 1, also right and mid, repeat step 1
        
        # 2. if mid, right > left, right == mid: 
        #    if a[mid + 1] > a[mid]: mid += 1, right += 1
        #    else: move only right
        
        # 3. right > mid > left: form a mountain
        #    move right to the right most point: stop when a[right] < a[j]
        #    res = max(res, right - left + 1), left = j, right = j
                
        while left < n - 2 and mid < n - 1 and right < n:
            
            if a[left] >= a[left + 1]:
                left += 1
                mid += 1
                right += 1
                continue
            
            else:
                #a[left] < a[left + 1]
                if a[mid + 1] > a[mid]:
                    mid += 1
                    right += 1
                    continue
                else:
                    #a[left] < a[left + 1], a[mid + 1] < a[mid]
                    if right < n - 1 and a[right + 1] < a[right]:
                        right += 1
                    else:
                        #update res:
                        if (right - left) > 1:
                            res = max(right - left + 1, res)
                            
                        left = right
                        mid, right = left, left
            
        return res
