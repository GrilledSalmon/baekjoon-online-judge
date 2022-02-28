from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return 2*n % 10000

def S(n):
    if n == 0:
        return 9999
    return n-1

def L(n):
    n_s = str(n).zfill(4)
    new_n_s = n_s[1:] + n_s[0]
    return int(new_n_s)

def R(n):
    n_s = str(n).zfill(4)
    new_n_s = n_s[-1] + n_s[:-1]
    return int(new_n_s)

def BFS(A, B):
    visited = [0]*10000
    visited[A] = ' '
    queue = deque([A])
    while not visited[B]:
        now_num = queue.popleft()
        for i, command in enumerate([D, S, L, R]):
            new_num = command(now_num)
            if not visited[new_num]:
                visited[new_num] = visited[now_num] + ['D', 'S', 'L', 'R'][i]
                queue.append(new_num)
    print(visited[B].strip())

def solve():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        BFS(A, B)

solve()