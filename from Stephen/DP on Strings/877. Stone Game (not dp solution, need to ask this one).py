class Solution:
    
    def stoneGame(self, piles: List[int]) -> bool:
        
        def pickedIndex(piles, i, j):
            
            if i == j:
                return i                        
            if piles[i] > piles[j]:  
                return i    
            elif piles[i] < piles[j]:
                return j
            elif piles[i] == piles[j]:
                if piles[i + 1] > piles[j - 1]:
                    return j
                else:
                    return i
                    
        n = len(piles)
        score = [0, 0]
        turn, i, j = 0, 0, n - 1
        
        while i <= j:            
            picked = pickedIndex(piles, i, j)
            
            if picked == i:
                i += 1
            else:
                j -= 1
                            
            if turn % 2 == 1:
                # Lee's turn:
                score[1] += piles[picked]
            else:
                # Alex's turn:
                score[0] += piles[picked]
                  
        return score[0] > score[1]        
