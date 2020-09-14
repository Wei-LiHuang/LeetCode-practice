
def solve(s):
    cur, maxLen = 0, 0
    for i in range(0, len(s)):
        if i == 0:            
            maxLen = 1
            cur = 1
        else:
            if s[i - 1] == s[i]:
                cur += 1
                maxLen = max(maxLen, cur)
            else:
                cur = 1

    print(maxLen)
            
                
if __name__ == '__main__':
    _str = input()    
    solve(_str)
