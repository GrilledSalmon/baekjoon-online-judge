from collections import deque

queue = deque()

queue.append('윤우')
queue.append('지용')
queue.append('기주')

print(queue)
print(queue[0])
print(queue[1])
print(queue.popleft())