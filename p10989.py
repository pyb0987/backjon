import sys
n = int(input())
result = [0]*10001
for i in range(n):
    result[int(sys.stdin.readline())]+=1
for a in range(10001):
    for _ in range(result[a]):
        print(a)