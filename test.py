import sys
input = sys.stdin.readline

def solve():
    M, N, H = map(int, input().split())
    tomato = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]

    ripen_tomato_coord = [] # 익은 토마토 위치
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 1:
                    ripen_tomato_coord.append((x, y, z))

    # BFS
    queue = ripen_tomato_coord
    day = -1
    while queue:
        temp = []
        day += 1
        for x, y, z in queue:
            probe = [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
            for x_, y_, z_ in probe:
                if 0<=x_<M and 0<=y_<N and 0<=z_<H and not tomato[z_][y_][x_]: # 좌표 만족 + 안 익었으면
                    tomato[z_][y_][x_] = 1
                    temp.append((x_, y_, z_))
        queue = temp
    
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if not tomato[z][y][x]: # 안 익은 토마토가 있다면
                    print(-1)
                    return

    print(day)
    return

solve()