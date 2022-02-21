import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

def check_coord(x, y, pre_root_):
    """경계조건, 이전 root가 아닌 조건을 충족하는지 확인"""
    if 0 <= x < M and 0 <= y < N and (x, y) != pre_root_:
        return True
    return False

maxi = [0]
def dfs_like(root:tuple, pre_root_=None, sum_=0, level_=0):
    x, y = root
    sum_ += paper[y][x]
    level_ += 1
    if level_== 4:
        if maxi[0] < sum_:
            maxi[0] = sum_
            # print(root, pre_root_, sum_)
        return

    coords = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] # 상하좌우
    for new_x, new_y in coords:
        if check_coord(new_x, new_y, pre_root_):
            dfs_like((new_x, new_y), root, sum_, level_)

    if level_ == 2: # 학교 모양
        for i in range(3):
            c1 = coords[i]
            if check_coord(c1[0], c1[1], pre_root_):
                for j in range(i+1, 4):
                    c2 = coords[j]
                    if check_coord(c2[0], c2[1], pre_root_):
                        temp_sum = sum_ + paper[c1[1]][c1[0]] + paper[c2[1]][c2[0]]
                        if maxi[0] < temp_sum:
                            maxi[0] = temp_sum

for y in range(N):
    for x in range(M):
        dfs_like((x, y))
print(maxi[0])