from collections import Counter

lst = [1, 2, 3, 4, 3, 2, 2, 2, 1, 0]

cnt = Counter(lst)

for i in cnt.keys():
    print(i, cnt[i])