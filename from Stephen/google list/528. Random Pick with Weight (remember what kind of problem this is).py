class Solution:

    def __init__(self, w: List[int]):        
        self.totalWeight = sum(w)        
        self.porpotions = [0]
        propotion = 0
        for i in range(0, len(w)):
            propotion += w[i]
            self.porpotions.append(propotion)            
        #print(self.porpotions)
            
                                
    def pickIndex(self) -> int:
        randPropotion = randrange(self.totalWeight)
        l, r = 0, len(self.porpotions) - 1
        while l <= r:            
            if l == r:
                return l                        
            elif r == l + 1:
                if randPropotion >= self.porpotions[l] and randPropotion < self.porpotions[r]:
                    return l
            else:
                mid = (l + r) // 2
                if randPropotion >= self.porpotions[l] and randPropotion < self.porpotions[mid]:
                    r = mid
                elif randPropotion >= self.porpotions[mid] and randPropotion < self.porpotions[r]:
                    l = mid                                                                                              
        return 0
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
