# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    arr = [None] + [1] * n

    for l in lost: arr[l] -= 1
    for r in reserve: arr[r] += 1

    for i in range(1, n + 1):
        if arr[i] == 0:
            if i - 1 != 0 and 0 <= i - 1 < n and arr[i - 1] > 1:
                arr[i - 1] -= 1
                arr[i] += 1
            elif 0 <= i + 1 <= n and arr[i + 1] > 1:
                arr[i + 1] -= 1
                arr[i] += 1
    return sum(map(lambda e: 1 if e != 0 else 0, arr[1:]))


if __name__ == '__main__':
    res = solution(5, [2, 4], [1, 3, 5])      # 5
    # res = solution(5, [2, 4], [3])            # 4
    # res = solution(3, [3], [1])               # 2
    # res = solution(10, [8, 10], [6, 7, 9])    # 10
    # res = solution(4, [3, 1, 2], [2, 4, 3])     # 3
    # res = solution(10, [5,4,3,2,1], [3,1,2,5,4])  # 10
    # res = solution(5, [1, 3], [2, 4])  # 5
    # res = solution(5, [3, 5], [2, 4])  # 5
    # res = solution(9, [2, 4, 7, 8], [3, 6, 9])  # 8
    # res = solution(5, [2, 4], [3, 5])  # 5

    print(res)