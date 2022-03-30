def main():
    from math import sqrt
    n = int(input())
    m = int(input())
    cache = [2,3]
    for i in range(4, m+1):
        pcount = 0
        for pnum in [x for x in cache if x<sqrt(i)+0.125]:
            if i%pnum == 0:
                pcount = 1
                break
        if pcount==0:
            cache.append(i)
    result = [x for x in cache if x<=m and x>=n]
    if len(result)==0:
        print(-1)
    else:
        print(sum(result),'\n',min(result), sep='')

main()