import sys
from collections import defaultdict
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

def bitZfill(string):
    while len(string) != 22: string = string[:2] + "0" + string[2:]
    return string

if __name__ == '__main__':
    n, m = map(int, input().split())
    train = [None] + ['0b' + '0' * 20] * n
    dic = defaultdict(int)

    for _ in range(m):
        command, *factors = map(int, input().split())

        if command == 1:
            t = bitZfill(bin(2 ** (factors[1] - 1)))
            train[factors[0]] = bitZfill(bin(int(train[factors[0]], 2) | int(t, 2)))
        elif command == 2:
            train[factors[0]] = bitZfill(bin(int(train[factors[0]], 2) & ((2 ** (factors[1] - 1)) ^ int('0b' + '1' * 20, 2))))
        elif command == 3:
            train[factors[0]] = train[factors[0]][:2] + train[factors[0]][3:]
            while len(train[factors[0]]) != 22: train[factors[0]] += "0"
        else:
            train[factors[0]] = bitZfill(bin(int(train[factors[0]], 2) >> 1))
    
    cnt = 0
    for i in range(1, n + 1):
        if not dic[train[i]]:
            cnt += 1
        dic[train[i]] += 1
    print(cnt)