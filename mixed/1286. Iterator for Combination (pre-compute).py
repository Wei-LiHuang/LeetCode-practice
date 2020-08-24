class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        a = []
        for c in characters:
            a.append(c)        
        self.len = combinationLength
                
        self.combination = []
        self.dfs(a, 0, "", self.len, self.combination)
        print(self.combination)
        self.index = 0
    
    def dfs(self, a, index, path, l, res):
        
        if len(path)  == l:
            res.append(path)
            return
        
        for i in range(index, len(a)):
            path += str(a[i])
            self.dfs(a, i + 1, path, l, res)
            path = path[0:len(path) - 1]                        
        return
        
                
    def next(self) -> str:
        res = self.combination[self.index]
        self.index += 1
        return res
        

    def hasNext(self) -> bool:
        if self.index < len(self.combination):
            return True
        
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
