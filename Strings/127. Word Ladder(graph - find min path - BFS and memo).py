# no solution: return 0
# begin word may not be in the wordList
# transformed word must be in the lsit
# hit -> hot
# hot -> dot, lot
# dot -> dog, lot or lot -> log, dot
# dog -> log, cog  or log -> dog, cog -> end

# since this question is a graph, we need a memo for memorizing the result
# if a node can't reach the target, then never try it again
# finding the minimum path to a node -> use BFS -> 


# start from start word, we create all the possible outcomes
# if the outcome is in the set, put into next step list

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def getChildren(parent: str, visited: set, wordListSet: set) -> List[str]:                       
            n = len(parent)
            res = []
            for i in range(0, n):                
                for c in range(ord('a'), ord('z') + 1):
                    fst = parent[:i]
                    mid = chr(c)
                    end = parent[i + 1:]
                    newChild = fst + mid + end                    
                    if newChild in wordListSet and newChild not in visited:
                        res.append(newChild)
                        visited.add(newChild)
            return res                
        visited = set()
        wordListSet = set()
        wordListSet.update(wordList)

        queue = [beginWord]
        res = 1
        while len(queue) > 0:
            curSize = len(queue)
            for i in range(0, curSize):
                curParent = queue.pop()
                if curParent == endWord:
                    return res
                children = getChildren(curParent, visited, wordListSet)
                queue = children + queue
            res += 1
        
        return 0
                
        
        
