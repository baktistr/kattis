# https://open.kattis.com/problems/cd
from sys import stdin

while True:
    n, m = map(int, stdin.readline().split())
    if n == 0 and m == 0:
        break

    # jack = [int(stdin.readline()) for _ in range(n)]
    # jill = [int(stdin.readline()) for _ in range(m)]

    # i, j, count = 0, 0, 0

    # while i < n and j < m:
    #     if jack[i] == jill[j]:
    #         count += 1
    #         i += 1
    #         j += 1
    #     elif jack[i] < jill[j]:
    #         i += 1
    #     else:
    #         j += 1

    # print(count)

    jack = set(int(stdin.readline()) for _ in range(n))
    jill = set(int(stdin.readline()) for _ in range(m))

    common_cds = jack.intersection(jill)

    print(len(common_cds))
