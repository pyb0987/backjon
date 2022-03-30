def stat(n, inp):
    from collections import Counter
    mean = int((((sum(inp)/n)*2)+1)//2)
    inp.sort()
    median = ((inp[n//2]+inp[n//2-1])/2 if n%2==0 else inp[(n-1)//2])
    modedict = Counter(inp)
    modeall = modedict.most_common()
    maximum = modeall[0][1]
    mode = []
    for i in modeall:
        if i[1]==maximum:
            mode.append(i[0])
        else:
            break
    mode.sort()
    rang = inp[-1]-inp[0]
    

    print(mean, median, mode[1] if len(mode)>1 else mode[0], rang, sep='\n')      


def main():
    import sys
    n= int(input())
    inp = []
    for i in range(n):
        inp.append(int(sys.stdin.readline().rstrip()))
    stat(n, inp)

main()