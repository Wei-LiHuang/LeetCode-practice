'''
    in1: max num
    in2: arr: 1 ~ max
'''

def solve(n, nums):

    s = set()
    for i in range(1, n + 1):
        s.add(i)
    for i in nums:
        s.remove(i)
    l = list(s)
    print(l[0])    


if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    solve(n, nums)
