# https://open.kattis.com/problems/greetingcard

from math import sqrt

n = int(input())

# store all point as set
points = set()
for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))

# find the all possible 2018 distance, using pytagoras formula a^2 + b^2 = c^2, where c = distance
c = 2018
displacements = []

# Generate all possible displacements
for a in range(1, int(sqrt(c ** 2 // 2)) + 1):
    b_squared = c ** 2 - a ** 2
    b = int(sqrt(b_squared))
    if b * b == b_squared:
        # Add all 8 combinations of a, b
        displacements.extend([(a, b), (-a, -b), (-a, b), (a, -b), (b, a), (-b, -a), (-b, a), (b, -a)])

# Add horizontal and vertical distances
displacements.extend([(c, 0), (0, c), (-c, 0), (0, -c)])

count = 0
for x, y in points:
    for dx, dy in displacements:
        if (x + dx, y + dy) in points:
            count += 1

print(count//2)  # Each pair is counted twice