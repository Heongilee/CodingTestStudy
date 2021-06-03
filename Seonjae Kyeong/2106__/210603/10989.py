import sys
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

INF = int(10e3) + 1
N = int(input())
cnt = [0] * INF

for _ in range(N):
    t = int(sys.stdin.readline())
    cnt[t] += 1


for i in range(INF):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)