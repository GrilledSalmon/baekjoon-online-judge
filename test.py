M = 6

set_1 = set([1])
conn_left = []

conn_list = sorted([sorted(list(map(int, input().split()))) for _ in range(M)])

while True:
    len_before = len(set_1)
    print(conn_list)
    for conn in conn_list:
        n1, n2 = conn
        if n1 in set_1 or n2 in set_1:
            set_1.update([n1, n2])
        else:
            conn_left.append(conn)
    
    # for문을 돌고 set_1의 변화가 없을 경우(추가로 1과 연결된 요소가 없을 경우)
    if len_before == len(set_1): 
        break
    else: # 처음 loop에서 선택받지 못한 애들 다시 돌려주기(1과 연결될 수 있는 새로운 가능성이 있으므로)
        conn_list = conn_left

print(len(set_1) - 1)