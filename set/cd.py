# https://open.kattis.com/problems/cd

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    jack = [int(input()) for _ in range(n)]
    jill = [int(input()) for _ in range(m)]

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
