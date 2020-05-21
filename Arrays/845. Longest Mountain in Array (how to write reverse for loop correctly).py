# 1. brute force: traversing all the points p in A, and if pi > pi -1 and p > pi + 1, p is a mountain of 3
# so if I maintain two lists call right and left:
# In right, ri means the number of continous smaller nodes. i.e. ri+1 > ri + 1 > ri + 2....
#   And we build from the end of the list, r n - 1, which is 0, then if rj > rj+1, rj = right[j] + 1, else right[j] = 0
# Left is the same, but starting from left.ArithmeticError
# Then we traverse the list again, if at ai, we have ri > 0 and li > 0, res[i] = r[i] + l[i] + 1

class Solution(object):
    def longestMountain(self, A):
        
        left = []
        for i in range(0, len(A)):
            if i == 0:
                left.append(0)
                continue
            if A[i] > A[i - 1]:
                left.append(left[i - 1] + 1)
            else:
                left.append(0)
        
        right = []
        for j in range(0, len(A)):
            i = len(A) - j - 1
            if i == len(A) - 1:
                right.append(0)
                continue
            if A[i] > A[i + 1]:
                right.append(right[j - 1] + 1)
            else:
                right.append(0)
                
        right.reverse()                
                                        
        res = 0
        for i in range(0, len(A)):         
            if left[i] > 0 and right[i] > 0:
                res = max(res, 1 + left[i] + right[i])
                
        return res
        
        
