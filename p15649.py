def main():
    import itertools
    n, m = tuple(map(int,input().split()))
    for elem in itertools.permutations([str(i) for i in range(1, n+1)], m):
        print(' '.join(elem))

main()