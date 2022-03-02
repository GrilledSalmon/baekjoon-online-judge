import sys
input = sys.stdin.readline

n = int(input())
tri = [tuple(map(lambda x: [int(x), None], input().split())) for _ in range(n)]

def solve(lev=0, i=0):
    """lev : 트리의 층(뿌리가 0층)
       i   : lev층 리스트의 인덱스"""
    if lev == n-1: # leaf 도달
        return tri[lev][i][0]
    if tri[lev][i][1] is None:
        now = tri[lev][i][0]
        tri[lev][i][1] = max((now + solve(lev+1, i), now + solve(lev+1, i+1)))
    return tri[lev][i][1]

print(solve())