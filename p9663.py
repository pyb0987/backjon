def Nqueen(n, list1):
    global count, number
    for i in range(number):
        if list1[0][i] and list1[1][n+i-1] and list1[2][i+number-n]:
            if n==1:
                count+=1
            else:
                list1[0][i], list1[1][n+i-1], list1[2][i+number-n] = False, False, False
                Nqueen(n-1, list1)
                list1[0][i], list1[1][n+i-1], list1[2][i+number-n] = True, True, True

def main():
    global number, count
    number = int(input())
    count = 0
    Nqueen(number, [[True]*number, [True]*(2*number-1), [True]*(2*number-1)])
    print(count)

main()