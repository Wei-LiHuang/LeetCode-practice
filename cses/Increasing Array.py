
def solve(n, arr):
    curIndex = 0
    res = 0
    while curIndex < len(arr):
        if curIndex == 0:
            curIndex += 1
            continue
        else:
            if arr[curIndex] < arr[curIndex - 1]:
                res += arr[curIndex - 1] - arr[curIndex]
                arr[curIndex] = arr[curIndex - 1]                    
            curIndex += 1

        #print(arr)
        
    print(res)


'''
n = 10
arr = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1]
solve(n, arr)
'''


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split(" ")]
    solve(n, arr)

