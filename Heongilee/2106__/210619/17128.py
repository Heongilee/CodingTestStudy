import sys
from functools import reduce
sys.stdin = open("./input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    myList = [0] * n
    
    for i in range(2, 4 - n - 2, -1):
        myList[i - 4 + n + 1] = reduce(lambda x, y: x * y, list(map(lambda j: A[j], range(i, i - 4, -1))))
    
    res = sum(myList)
    for q in Q:
        for j in range(q, q - 4, -1):
            myList[j - 1] *= -1
            res += myList[j - 1] * 2
        print(res)