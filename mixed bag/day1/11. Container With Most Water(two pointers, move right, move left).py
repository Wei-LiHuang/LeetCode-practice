# brute force: list out all the possible area by:
# for i in range(n - 1, -1, -1), j in rnage(n - 1, i - 1, -1)
# -> res = max ( res, min(h[i], h[j]) * (j - i))
# runtime: O(n + n - 1 + n - 2 + ...) -> O(N^2), space: O(N^2)

# how to get faster?
# f法無效, 過去的結果不能解決現在的問題 -> 改用觀察答案間的關係
# water = min(li, lj) * (j - i) -> 從寬度下手
# 從最寬 i = 0, j = n - 1 開始 -> 則 瓶頸為 min(li, lj)

class Solution:
    def maxArea(self, a: List[int]) -> int:
        
        n = len(a)
        i, j = 0, n - 1
        res = -float('inf')
        while i < j:
            
            area = min(a[i], a[j]) * (j - i)
            res = max(res, area)
            
            if a[i] == a[j]:
                i += 1
                j -= 1
            elif a[i] < a[j]:
                i += 1
            elif a[i] > a[j]:
                j -= 1
        
        return res
                
            
