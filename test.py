from collections import deque

queue = deque()

queue.append('윤우')
queue.append('지용')
queue.append('기주')

print(queue)
print(queue[0])
print(queue[1])
print(queue.popleft())

list_a = [1, 2, 3]
list_b = [4, 5, 6]

print([(a, b) for a in list_a for b in list_b])