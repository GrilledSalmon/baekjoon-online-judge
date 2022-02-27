import re
N, M = int(input()), int(input())
S = input()

p_n = 'I' + 'OI'*N
regex = re.compile(f'{p_n}(OI)*')
ans = 0
for r in re.finditer(regex, S):
    l = (len(r.group()) - 1) // 2
    ans += l - N + 1
print(ans)