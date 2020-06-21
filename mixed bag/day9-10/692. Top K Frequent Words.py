# try 1: word -> count, count -> word list, push to res
# runtime: O(N) space: O(2N) -> O(N)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
                        
        _dict = dict()
        
        for w in words:
            if w in _dict:
                _dict[w] += 1
            else:
                _dict[w] = 1
                
        countToWord = dict()
        for key, val in _dict.items():            
            if val in countToWord:
                countToWord[val].append(key)
            else:
                countToWord[val] = [key]
                
        res = []
        for count in range(len(words), -1, -1):
            
            if count in countToWord:
                add = countToWord[count]
                add.sort()
                
                if len(res) + len(add) <= k:
                    res.extend(add)
                else:
                    diff =  k - len(res)
                    add = add[0: diff]
                    res.extend(add)
                    
            if len(res) == k:
                break
                                        
        return res
