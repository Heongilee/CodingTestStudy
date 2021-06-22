import sys
from math import factorial as f
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        print(f(m) // (f(n) * f(m - n)))