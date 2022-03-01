import sys
input = sys.stdin.readline
N = int(input())
img = [input() for _ in range(N)]

def compr(x=0, y=0, n=N, img=img):
    if n == 1:
        return img[y][x]
    
    n //= 2
    part1 = compr(x, y, n)
    part2 = compr(x+n, y, n)
    part3 = compr(x, y+n, n)
    part4 = compr(x+n, y+n, n)
    part = part1 + part2 + part3 + part4
    if part == '0000':
        return '0'
    elif part == '1111':
        return '1'
    else:
        return f'({part})'

print(compr())