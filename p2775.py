def apart(tup):
    result = []
    for i in range(len(tup)):
        k, n = tup[i]
        popul = (list(range(1,n+1)))
        for _ in range(k):
            for j in range(n-1, -1,-1):
                popul[j]=sum(popul[0:(j+1)])
        result.append(str(popul[n-1]))
    print('\n'.join(result))


def main():
    n = int(input())
    tmp = []
    for i in range(n):
        k = int(input())
        j = int(input())
        tmp.append([k,j])
    apart(tmp)


main()