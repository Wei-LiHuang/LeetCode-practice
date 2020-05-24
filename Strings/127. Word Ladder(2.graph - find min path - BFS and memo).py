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
    
        def getNext(current: str, visited: set, wordListSet: set):            
            
            visited.add(current)
            n = len(current)
            
            res = []
            for i in range(0, n):
                for j in range(ord('a'), ord('z') + 1):
                    c = chr(j)
                    word = current[:i] + c + current[i + 1:]
                    if word not in visited and word in wordListSet:
                        res.append(word)
                                                                
            return res
                
        wordListSet = set(wordList)
        if endWord not in wordListSet:
            return 0
        
        stack, visited = [beginWord], set()
        step = 1
        while len(stack) != 0:
            curSize = len(stack)
            for i in range(0, curSize):                
                curWord = stack.pop()
                if curWord == endWord:
                    return step
                if curWord in visited:
                    continue
                nextWords = getNext(curWord, visited, wordListSet)
                stack = nextWords + stack
            step += 1
            
        return 0
            
