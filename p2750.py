def sort1000(n, tup):
    result = ['' for i in range(2001)]
    for i in range(n):
        result[tup[i]+1000]=tup[i]
    for i in result:
        if i!='':
            print(i)

def main():
    n = int(input())
    tup = [int(input()) for i in range(n)]
    sort1000(n, tup)

main()