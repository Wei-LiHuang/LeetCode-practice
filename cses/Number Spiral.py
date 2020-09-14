
def solve(t, tests):
    res = []
    for test in tests:
        x, y = test[0] - 1, test[1] - 1

        diagonal = 1
        pos = max(x, y)
        diagonal = pos * pos + pos + 1

        if x == y:
            res.append(diagonal)

        elif pos > y:            
            if pos % 2 == 0:                    
                diagonal -= (pos - y)
            else:
                diagonal += (pos - y)
            res.append(diagonal)
            
        elif pos > x:
            if pos % 2 == 1:                    
                diagonal -= (pos - x)
            else:
                diagonal += (pos - x)
            res.append(diagonal)
   
    print(*res)

if __name__ == '__main__':
    t = int(input())
    tests = []
    for i in range(0, t):
        arr = [int(i) for i in input().split(" ")]
        tests.append(arr)
    solve(t, tests)

