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
    
        def findChildren(w: str, visited: set, wordListSet: set):
            children = []
            for i in range(0, len(w)):
                for j in range(0, 26):
                    child = w[:i] + chr(j + ord('a'))+w[(i + 1):]
                    if child not in visited and child in wordListSet:
                        children.append(child)
            return children
        
        visited, wordListSet, stack = set(), set(wordList), [beginWord]
        if endWord not in wordListSet:
            return 0
        
        res = 0
        while len(stack) > 0:
            curSize = len(stack)
            children = []
            for i in range(0, curSize):
                cur = stack.pop()
                if cur == endWord:
                    return res + 1
                if cur not in visited:
                    visited.add(cur)
                    children.extend(findChildren(cur, visited, wordListSet))                                
            stack = children                    
            res += 1
                                                            
        return 0
                       
