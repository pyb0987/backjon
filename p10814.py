def main():
    import sys
    n= int(input())
    inp = []
    for i in range(n):
        inp.append(sys.stdin.readline().rstrip().split())
    res = sorted(inp, key = lambda x : int(x[0]))
    print('\n'.join([str(x[0])+' '+str(x[1]) for x in res]))

main()