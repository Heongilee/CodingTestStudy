import sys
sys.stdin = open("./input.txt", "rt")
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
if __name__ == '__main__':
    m, n, h = map(int, input().split()) # 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100
    board = []
    dist = [[[0] * m for _ in range(n)] for _ in range(h)]
    res = 0

    for _ in range(h): board.append([list(map(int, input().split())) for _ in range(n)])
    dq = deque([(i, j, k) for i in range(h) for j in range(n) for k in range(m) if board[i][j][k] == 1])

    while dq:
        i, j, k = dq.popleft()
        
        for l in range(6):
            ii = i + dz[l]
            jj = j + dx[l]
            kk = k + dy[l]

            if 0 <= ii < h and 0 <= jj < n and 0 <= kk < m and board[ii][jj][kk] == 0:
                board[ii][jj][kk] = 1
                dist[ii][jj][kk] = dist[i][j][k] + 1
                if dist[ii][jj][kk] > res: res = dist[ii][jj][kk]
                dq.append((ii, jj, kk))

    print(-1 if any (board[i][j][k] == 0 for i in range(h) for j in range(n) for k in range(m)) else res)