#   depend on the realtion between the target and elements:    
#   from: https://github.com/Deadbeef-ECE/Interview/blob/master/Leetcode/BackTracking/039_Combination_Sum.java
#    // O(k * 2^n') time:
#    // 此题可以转换成 combination sum II, 如何做呢, 举个栗子:
#    // int[] arr = {2, 3, 4, 5, 6}, target = 10; 我们知道此题中,每个元素可以重复用, 
#    // 其实, 如果把 arr 变成 {2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6}, 然
#    // 后每个元素只能用一次, 就变成了combination sum II的要求了. 
#    // 我们再看新数组, 元素多了很多, 多了多少? 
#    // 那就是数组中所有小于等于target的元素E增加了ceil(target/E)个, 然后就可以用
#    // combination sum II的方法分析复杂度了. 这里n'是新arr的大小

class Solution:
    
    def combinationSum(self, a: List[int], tgt: int) -> List[List[int]]:
        
        def dfs(a, s, tgt, path, curSum, res):
                        
            if curSum == tgt: 
                res.append(list(path))
                
            if curSum < tgt:                
                for i in range(s, len(a)):
                    if curSum + a[i] <= tgt:   # 提升速度
                        path.append(a[i])
                        dfs(a, i, tgt, path, curSum + a[i], res)
                        path.pop()            
            return
        
        
        n = len(a)
        if n == 0:
            return []
        
        #a.sort()
        res = []
        dfs(a, 0, tgt, [], 0, res)
        
        return res
            
