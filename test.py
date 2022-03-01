import sys
input = sys.stdin.readline

def print_list(ls):
    print('[' + ','.join(map(str, ls)) + ']')

def solve():
    p = input().rstrip()
    n = int(input())
    try:
        nums = list(map(int, input().strip('[]\n').split(',')))
    except ValueError:
        nums = []

    rev = 0
    s, e = 0, n
    for command in p:
        if command == 'R':
            rev = 1-rev
        else:
            if rev: # 뒤집어졌으면
                e -= 1
            else: # 똑바로 돼 있으면
                s += 1
        if s > e:
            print('error')
            return
    if rev:
        if s == 0:
            print_list(nums[e-1::-1])
        else:
            print_list(nums[e-1:s-1:-1])
    else:
        print_list(nums[s:e])
    return

T = int(input())
for _ in range(T):
    solve()