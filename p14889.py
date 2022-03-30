import sys
import itertools
n = int(input())
stats = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
minimum = sys.maxsize
c = list(itertools.combinations(set(range(n)), n//2))
for i in range(len(c)//2):
    div1 = c[i]
    div2 = c[-i-1]
    totalsum1, totalsum2 = 0, 0
    for i, j in itertools.permutations(div1, 2):
        totalsum1 += stats[i][j]
    for i, j in itertools.permutations(div2, 2):
        totalsum2 += stats[i][j]
    minimum = min(abs(totalsum1-totalsum2), minimum)
print(minimum)