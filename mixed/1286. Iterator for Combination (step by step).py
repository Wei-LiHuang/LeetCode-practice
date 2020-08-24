class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):        
        self.c = characters
        self.len = combinationLength
        self.index = [0] * self.len
        for i in range(0, self.len):
            self.index[i] = i            
        self.res = characters[0:self.len]
        self.isLast = False
        
        if len(characters) == self.len:
            self.isLast = True
                
    def next(self) -> str:                        
        ans = self.res
        #print(ans)
                
        change = False
        for i in range(self.len - 1, -1, -1):            
            
            if self.index[i] < len(self.c) - (self.len - i):
                self.index[i] += 1
                if not change:
                    self.res = self.res[0:i] + self.c[self.index[i]] + self.res[i + 1:self.len]                
                elif change:
                    self.res = self.res[0:i] + self.c[self.index[i]]
                    for j in range(i + 1, self.len):
                        self.index[j] = self.index[j - 1] + 1       
                        self.res += self.c[self.index[j]]
                break            
            else:
                change = True
        
        if ans == self.res:
            self.isLast = True
                        
        return ans
        
                
    def hasNext(self) -> bool:   
        return not self.isLast
                
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
