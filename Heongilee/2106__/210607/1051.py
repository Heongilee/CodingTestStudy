import sys
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]

    for s in range(min(n, m), 0, -1):
        dx = [s - 1, 0, s - 1]
        dy = [0, s - 1, s - 1]
        for i in range(n - s + 1):
            for j in range(m - s + 1):
                if all (board[i][j] == board[i + dx[k]][j + dy[k]] for k in range(3)):
                    print(s ** 2)
                    sys.exit(0)