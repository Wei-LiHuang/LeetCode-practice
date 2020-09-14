def solve(n):

    res = []
    if n == 1:
        print(1)
    
    elif n <= 3:
        print("NO SOLUTION")
    else:
        first = []
        for v in range(1, n + 1):
            if v % 2 == 0:
                first.append(v)
        second = []
        for v in range(1, n + 1):
            if v % 2 == 1:
                second.append(v)
        res = first + second
            
        print(*res)


if __name__ == '__main__':
    n = int(input())
    solve(n)

