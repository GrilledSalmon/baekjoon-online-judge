import sys
input = sys.stdin.readline
M = int(input())

S = set()

def add(x): S.add(x)

def remove(x): S.discard(x)

def check(x):
    return print(1) if x in S else print(0)

def toggle(x):
    if x in S:
        remove(x)
    else:
        add(x)

def all(x):
    S.update(range(1,21))

def empty(x): S.clear()

def operate(command, x):
    func_dic = {
        'add' : add,
        'remove' : remove,
        'check' : check,
        'toggle' : toggle,
        'all' : all,
        'empty' : empty
    }
    func_dic[command](x)

for _ in range(M):
    try: 
        inp = input().split()
        command = inp[0]
        x = int(inp[1])
    except: x = None
    
    operate(command, x)