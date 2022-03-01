import sys
input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

def find_baby_shark():
    """아기상어 위치 찾고 -1로 바꿔줌(방문 처리)"""
    for y in range(N):
        for x in range(N):
            if space[y][x] == 9:
                space[y][x] = -1
                return x, y

class baby_shark:
    """아기 상어"""
    def __init__(self):
        """아기 상어 크기, 위치, 먹은 횟수, 배부름"""
        self.size = 2
        self.full = 0
        self.eat_count = 0
        self.coord = find_baby_shark()
    
    def eat(self, fish_coord):
        """fish_coord 위치의 물고기 냠"""
        if self.size-1 == self.full:
            self.size += 1
            self.full = 0
        else:
            self.full += 1
        self.coord = fish_coord
        self.eat_count += 1
        space[fish_coord[1]][fish_coord[0]] = 0

baby_shark = baby_shark()
baby_shark.size, baby_shark.full, baby_shark.eat_count, baby_shark.coord

def prior_fish(fishes_coord) -> tuple:
    """가장 가까운 물고기들 중 가장 우선으로 먹을 물고기 위치 리턴"""
    return min(fishes_coord, key=lambda x: (x[1],x[0]))

def closest_fish():
    """가장 가까운 물고기의 위치와 거리 리턴"""
    queue = [baby_shark.coord]
    fishes_coord = []
    distance = 0
    same_size_fish_set = set()
    while queue:
        distance += 1
        temp = []
        for x, y in queue:
            probe = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for x_, y_ in probe:
                if not (0<=x_<N and 0<=y_<N): # 좌표 범위 조건
                    continue
                
                status = space[y_][x_]
                
                # 먹을 수 있는 조건
                if 0 < status < baby_shark.size: 
                    fishes_coord.append((x_, y_))
                
                # 먹지도 못하고 지나가지도 못하는 조건(먹을 수 있는 물고기 발견 or 물고기 큼 or 이미 방문)
                elif fishes_coord or status > baby_shark.size or status == -(baby_shark.eat_count + 1):
                    continue
                
                # 지나갈 수 있는 조건(사이즈 같음 or 지나간 적 없음)
                else:
                    if status == baby_shark.size:
                        if (x_, y_) in same_size_fish_set: # 이미 방문한 적이 있다면
                            continue
                        else: # 방문표시 해주기
                            same_size_fish_set.add((x_, y_))
                    else: # 물고기가 없고 방문한 곳 표시
                        space[y_][x_] = -(baby_shark.eat_count + 1) 
                    temp.append((x_, y_)) # 아기상어가 새출발 할 위치 추기

        if fishes_coord: # 먹을 수 있는 물고기가 있으면
            return prior_fish(fishes_coord), distance
        queue = temp
    return None, 0

def solve():
    time = 0
    while True:
        fish_coord, distance = closest_fish()
        if fish_coord is None:
            break
        time += distance
        baby_shark.eat(fish_coord)
    return time

print(solve())

# for i in range(N):
#     for j in range(N):
#         print(space[i][j], end = ' ')
#     print()