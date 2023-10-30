# https://open.kattis.com/problems/cd
from sys import stdin

while True:
    n, m = map(int, input().split())
    # n, m = map(int, stdin.readline().split())
    if n == 0 and m == 0:
        break

    # jack = [int(input()) for _ in range(n)]
    # jill = [int(input()) for _ in range(m)]
    jack = [int(stdin.readline()) for _ in range(n)]
    jill = [int(stdin.readline()) for _ in range(m)]

    # jack = []
    # for _ in range(n):
    #     jack.append(int(stdin.readline()))

    # jill = []
    # for _ in range(m):
    #     jill.append(int(stdin.readline()))

    i, j, count = 0, 0, 0

    while i < n and j < m:
        if jack[i] == jill[j]:
            count += 1
            i += 1
            j += 1
        elif jack[i] < jill[j]:
            i += 1
        else:
            j += 1

    print(count)
