import sys
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

INF = int(10e8)
def compare(K):
    cnt, bal = 1, 0
    for i in range(n):
        if bal + arr[i] <= K:
            bal += arr[i]
        else:
            bal = arr[i]
            cnt += 1
    return cnt

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    res = None

    lt, rt = max(arr), INF
    while lt <= rt:
        mid = (lt + rt) // 2

        t = compare(mid)
        if t > m:
            lt = mid + 1
        else:
            res = mid
            rt = mid - 1
    print(res)