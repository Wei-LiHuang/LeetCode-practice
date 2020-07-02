#runtime: O(NlgN) or O(N * l), l = l = max len(word)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
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
