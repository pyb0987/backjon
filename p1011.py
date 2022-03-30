def hop(tup):
    result = []
    for i in range(len(tup)):
        n, m = tuple(map(int, tup[i]))
        hopdistance = 0
        hopturn = 0
        hopmax = 1
        while m-n>hopdistance:
            hopturn += 1
            hopdistance += hopmax
            if (m-n<=hopdistance): break
            hopturn += 1
            hopdistance += hopmax
            hopmax +=1            
        result.append(str(hopturn))
    print('\n'.join(result))

def main():
    n = int(input())
    inp = []
    for i in range(n):
        inp.append(input().split())
    hop(inp)

main()