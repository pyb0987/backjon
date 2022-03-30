def dungchi(n, tup):
    result = []
    for i in range(n):
        tmp = [(tup[i][0]<one[0])+(tup[i][1]<one[1]) for one in tup]
        result.append(str(tmp.count(2)+1))  
    print(' '.join(result))


def main():
    n = int(input())
    inp = []
    for i in range(n):
        inp.append(tuple(map(int, input().split())))
    dungchi(n, inp)

main()