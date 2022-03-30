n, k = int(input()), [0, 1, 2, 1, 2]
print(-1 if (n==4 or n==7) else n//5 + k[n%5])