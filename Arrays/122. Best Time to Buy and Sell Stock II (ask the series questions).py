# buy on day i: for i+1 ~ n-1 => we can make p(i, i+1) or p(i, i+2) ... p(i, n - 1)
# so if buy in a, b, c ,d day: total = p(a, s1) + p(b, s2) + p(c, s3) + p(d, s4)
# b > s1, c > s2, d > s3, n - 1 >= s4
# p(x, y) = price[y] - price[x]
# to get max profit: get every positive p(i, j)

class Solution(object):

    def maxProfit(self, a):
        
        n = len(a)
        b = 0
        s = 0
        res = 0
        
        for i in range(1, n):
                    
            if b < i and a[i] < a[b]:
                b = i
                continue
                
            if b < i and a[i] > a[b]:
                if i == n - 1:
                    res += a[i] - a[b]
                else:
                    if a[i] > a[i + 1]:
                        res += a[i] - a[b]
                        b = i + 1                
        return res
