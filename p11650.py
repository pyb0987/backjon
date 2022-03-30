def main():
    import sys
    n= int(input())
    inp = []
    for i in range(n):
        inp.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
    res = sorted(inp)
    print('\n'.join([str(x[0])+' '+str(x[1]) for x in res]))

main()