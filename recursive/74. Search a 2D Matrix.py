class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearchInRow (a: List[int], left: int, right: int, tgt: int) -> bool:          
            if right < left:
                return False
            
            if left == right:
                if a[left] == tgt:
                    return True
                else:
                    return False
            elif right - 1 == left:
                if a[left] == tgt:
                    return True
                elif a[right] == tgt:
                    return True
                else:
                    return False
            else:
                mid = int((left + right)/2)
                if a[mid] == tgt:
                    return True
                elif a[mid] < tgt:
                    return binarySearchInRow(a, mid + 1, right, tgt)
                else:
                    return binarySearchInRow(a, 0, mid - 1, tgt)
        
        def searchRow(m: List[List[int]], tgt: int):
            maxR = len(m)
            if maxR == 0:
                return False
            for r in range(0, maxR):
                maxC = len(m[r]) - 1
                if maxC < 0:
                    continue
                mmin = m[r][0]
                mmax = m[r][maxC]
                if tgt >= mmin and tgt <= mmax:
                    return binarySearchInRow(m[r], 0, maxC, tgt)
            return False
            
            
        return searchRow(matrix, target)
