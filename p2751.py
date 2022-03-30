def sort2(n, tup):
    import math
    level = math.ceil(math.log2(n))
    for i in range(1, level+1):
        for j in range(2**(level-i)):
            a_start, b_start = min(n-1, j*2**i), min(n-1, j*2**i+2**(i-1))
            a_end, b_end = b_start, min(n, (j+1)*2**i)
            tmp = []
            while True:
                if b_start>=b_end:
                    for k in range(a_start, a_end):
                        tmp.append(tup[k])
                    break
                if a_start>=a_end:
                    for k in range(b_start, b_end):
                        tmp.append(tup[k])
                    break
                if tup[a_start]>=tup[b_start]:
                    tmp.append(tup[a_start])
                    a_start += 1
                else:
                    tmp.append(tup[b_start])
                    b_start += 1
            tup[min(n-1, j*2**i):b_end]=tmp
    print('\n'.join(map(str, list(reversed(tup)))))


def main():
    import sys
    n = int(input())
    tup = [int(sys.stdin.readline()) for i in range(n)]
    sort2(n, tup)

main()