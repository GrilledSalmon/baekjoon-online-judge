import sys
input = sys.stdin.readline

def solve():
    k_set = {x + p*M for p in range(N)}
    for q in range(M):
        k = y + q*N
        if k in k_set:
            return k
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solve())