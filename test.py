import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# BFS?
def bfs():
    queue = [(0, 0)]
    miro[0][0] = 0
    step = 1
    while True:
        temp = []
        step += 1
        for x, y in queue:
            probe = []
            if y != 0:   probe.append((x, y-1)) # 상
            if y != N-1: probe.append((x, y+1)) # 하
            if x != 0:   probe.append((x-1, y)) # 좌
            if x != M-1: probe.append((x+1, y)) # 우
            
            for adj_x, adj_y in probe:
                if (adj_x, adj_y) == (M-1, N-1):
                    return step
                elif miro[adj_y][adj_x]:
                    miro[adj_y][adj_x] = 0
                    temp.append((adj_x, adj_y))
        queue = temp
print(bfs())