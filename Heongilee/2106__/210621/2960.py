import sys
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())    # 1 ≤ K < N, max(2, K) < N ≤ 1000
    board = [True] * (n + 1)
    board[0] = board[1] = False       # 문제 푸는데 상관 없음.
    cnt = 0
    
    while True:
        p = 2
        while not board[p]: p += 1

        for i in range(p, n + 1, p):
            if board[i]:
                board[i] = False
                cnt += 1
                if cnt == k:
                    print(i)
                    sys.exit(0)