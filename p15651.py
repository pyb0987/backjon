def main():
    import itertools
    n, m = tuple(map(int,input().split()))
    for elem in itertools.combinations_with_replacement([str(i) for i in range(1, n+1)], m):
        print(' '.join(elem))

main()