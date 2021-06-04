import sys
from collections import defaultdict
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

INF = int(10e9)
if __name__ == '__main__':
    n, m = map(int, input().split())
    dnas = [input().rstrip() for _ in range(n)]
    hammingDist = 0
    S = ""

    for i in range(m):
        myList = []
        tmp = [dnas[j][i] for j in range(n)]
        dic = defaultdict(int)
        for e in tmp: dic[e] += 1
        for k, v in dic.items():
            myList.append((k, v))

        myList.sort(key=lambda X: (-X[1], X[0]))
        hammingDist += sum(map(lambda j : 1 if myList[0][0] != tmp[j] else 0, range(n)))
        S += myList[0][0]
    print(S)
    print(hammingDist)