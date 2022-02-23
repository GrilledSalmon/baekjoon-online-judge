N = input()
M = int(input())
brk_buttons = list(map(int, input().split())) if M else []

def possible(num:str, butt_set:set):
    """num을 butt_set에 있는 수로 만들 수 있는지 확인"""
    if num is None:
        return True
    for s in num:
        if int(s) not in butt_set:
            return False
    return True


# 살아 있는 버튼으로 가장 비슷한 수 만들기
def sim_num_fun() -> tuple:
    """살아 있는 버튼으로 만들 수 있는 N과 가장 가까운 수 리턴"""
    butt_set = {i for i in range(10) if i not in brk_buttons}
    max_butt, min_butt = max(butt_set), min(butt_set)
    sim_num_list = []
    print(N, butt_set)
    for i, n in enumerate(N):
        if int(n) in butt_set:
            sim_num_list.append(n)
        else:
            unders = [b for b in butt_set if b < int(n)] # 더 작은 버튼들
            overs = [b for b in butt_set if b > int(n)] # 더 큰 버튼들
            closest_under = str(max(unders)) if unders else None # 버튼이 없는 경우 고려
            closest_over = str(min(overs)) if overs else None
            
            prev_num = int(''.join(sim_num_list)) if sim_num_list else None # sim_num_list가 비어 있는 경우 고려
            if closest_under is None:
                sim_num_1 = ''.join(sim_num_list) + closest_over + str(min_butt)*(len(N)-i-1)
                temp = str(prev_num - 1) if prev_num is not None else None
                if temp is None:
                    if len(N) == 1:
                        sim_num_2 = '100000'
                    else:
                        sim_num_2 = str(max_butt)*(len(N)-i-1)
                elif temp == '0':
                    sim_num_2 = str(max_butt)*(len(N)-i)
                elif possible(temp, butt_set):
                    sim_num_2 = temp + str(max_butt)*(len(N)-i)
                else:
                    sim_num_2 = sim_num_1
            elif closest_over is None:
                sim_num_1 = ''.join(sim_num_list) + closest_under + str(max_butt)*(len(N)-i-1)
                temp = str(prev_num + 1) if prev_num else '1'
                if possible(temp, butt_set):
                    sim_num_2 = temp + str(min_butt)*(len(N)-i)
                else:
                    sim_num_2 = sim_num_1
            else: # 둘 다 존재(둘 다 없을 수 는 없음)
                sim_num_1 = ''.join(sim_num_list) + closest_under + str(max_butt)*(len(N)-i-1)
                sim_num_2 = ''.join(sim_num_list) + closest_over + str(min_butt)*(len(N)-i-1)
            print(sim_num_1, sim_num_2)
            return int(sim_num_1), int(sim_num_2)
    sim_num = int(''.join(sim_num_list))
    return sim_num, sim_num
    

if M == 10: # 버튼 다 고장난 경우
    print(abs(100-int(N)))
else:
    sim_num_1, sim_num_2 = sim_num_fun()
    print(sim_num_1, sim_num_2)
    candi_1 = abs(sim_num_1 - int(N)) + len(str(sim_num_1))
    candi_2 = abs(sim_num_2 - int(N)) + len(str(sim_num_2))
    candi_3 = abs(100 - int(N))
    print(min([candi_1, candi_2, candi_3]))