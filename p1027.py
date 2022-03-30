def building(n, tup):
    import sys
    resultmax = 0
    for i in range(n):
        left = [sys.maxsize, 0]
        right = [-sys.maxsize, 0]
        for j in range(i-1, -1, -1):
            if left[0]>(tup[i] - tup[j])/(i-j):
                left[0] = ((tup[i] - tup[j])/(i-j))
                left[1]+=1
        for j in range(i+1, n):
            if right[0]<(tup[j] - tup[i])/(j-i):
                right[0] = (tup[j] - tup[i])/(j-i)
                right[1]+=1
        resultmax = max(left[1]+right[1], resultmax)
    print(resultmax)
        
def main():
    n = int(input())
    inp = tuple(map(int,input().split()))
    building(n, inp)

main()



    