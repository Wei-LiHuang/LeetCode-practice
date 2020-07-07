#runtime: O(NlgN) or O(N * l), l = l = max len(word)
class Solution:         
    
    def longestStrChain(self, words: List[str]) -> int:
        
        def cmp(w1, w2):
            return len(w2) - len(w1)
        
        def getNext(w):
            res = set()
            for i in range(0, len(w)):
                res.add(w[0 : i] + w[i + 1: len(w)])
            return res
        
        words.sort(key = cmp_to_key(cmp))
        
        #print(words)
        '''
        dp[i]: length of the longest str chain end at words[i]                
        dp[i] = 1 + max(dp[k], for all words[k] that is words[i]'s next)        
        '''
        
        n, res, dp = len(words), 0, dict()
        for i in range(n - 1, -1, -1):
            dp[words[i]] = 1
            _nexts = getNext(words[i])
            for _next in _nexts:
                if _next in dp:
                    dp[words[i]] = max(dp[words[i]], 1 + dp[_next])
                
            res = max(res, dp[words[i]])
                
        return res
        
        
        
    
    def longestStrChain1(self, words: List[str]) -> int:
        
        # O(1)
        def cmp (w1, w2):
            l1, l2 = len(w1), len(w2)
            return l1 - l2
        
        # O(l), l = len(cur)
        def findNext(cur, _set, count, res):
            n = len(cur)    
            for i in range(0, n):
                _next = cur[0:i] + cur[i + 1 : n]
                if _next in _set:
                    count[_next] = max(count[_next], 1 + count[cur])
                    res[0] = max(res[0], count[_next])
            return
        
        
        if len(words) == 0:
            return 0
        
        # O(N lgN)
        words = sorted(words, key = cmp_to_key(cmp))
        
        # O(N)
        _set, count = set(), dict()
        for w in words:
            _set.add(w)
            count[w] = 1
        
        res = [1]
        n = len(words)
        # O(N * l)
        for i in range(n - 1, -1, -1):
            findNext(words[i], _set, count, res)
                        
        return res[0]
