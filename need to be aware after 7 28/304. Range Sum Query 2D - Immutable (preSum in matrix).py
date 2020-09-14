class NumMatrix:

    def __init__(self, a: List[List[int]]):
        self.m = len(a)
        if self.m == 0:
            return
        self.n = len(a[0])
        
        self.d = []
        for i in range(0, self.m + 1):
            self.d.append([0] * (self.n + 1))
            
        for i in range(0, self.m):
            for j in range(0, self.n):
                self.d[i + 1][j + 1] = self.d[i + 1][j] + self.d[i][j + 1] + a[i][j] - self.d[i][j]
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.d[r2 + 1][c2 + 1] - self.d[r1][c2 + 1] - self.d[r2 + 1][c1] + self.d[r1][c1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
