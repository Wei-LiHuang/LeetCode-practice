# try 1:
# n = 0: ""
# n = 1:  ()
# n = 2:  (()), ()()
# n = 3:  ((())), (()()), ()(()), (())(), ()()()
# n = 4:  (((()))), ((()())), (()(())), ((())()), (()()())
#         ()((())), ()(()()), ()()(()), ()(())(), ()()()()
#         ((()))(), (()())(), "()(())()", (())()(), "()()()()" ----> and (())(())
# take the previous set of parenthesises, add a pair at the outside, add a left pair, add a right pair ----> wrong, can't generate cases like (())(())

# try 2:
# dfs(leftP, rightP) -> generate tree, add res when use it all
# do we need a function to check is the parenthesis is valid? no, only gererate correct pair.

# ""
# (: (( or () 
# ): end

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(path: str, l: int, r: int, res: List[str]):
            
            if l == 0 and r == 0:
                res.append(path)
                return
            
            if l > 0:
                dfs(f'{path}(', l - 1, r, res)
            
            if r > l:
                dfs(f'{path})', l, r - 1, res)
            
            return
            
                        
        res = []
        dfs("", n, n, res)                            
        return res
    
    
