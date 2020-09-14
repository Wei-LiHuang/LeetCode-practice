class Solution:
    def smallerNumbersThanCurrent(self, a: List[int]) -> List[int]:
        
        count = [0] * 101 # 0 ~ 100
        for val in a:
            count[val] += 1
            
        for i in range(1, 101):
            count[i] += count[i - 1]
            
        res = [0] * len(a)
        for i in range(0, len(a)):
            if a[i] == 0:
                res[i] = 0
            else:
                res[i] = count[a[i] - 1]
        
        return res
