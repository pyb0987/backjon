def hotel(tup):
    result = []
    for i in range(len(tup)):
        h, w, n = tuple(map(int, tup[i]))
        result.append('%d%02d'%(h if n%h==0 else n%h ,(n-1)//h+1))
    print('\n'.join(result))

def main():
    n = int(input())
    tmp = []
    for i in range(n):
        tmp.append(input().split())
    hotel(tmp)


main()