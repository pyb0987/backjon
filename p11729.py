def hanoi(n,start=1, via=2, end=3, result=[]):
    if n==1:
        result.append('%d %d'%(start, end))
    if n>1:
        hanoi(n-1, start, end, via, result)
        result.append('%d %d'%(start, end))
        hanoi(n-1, via, start, end, result)
    return result
 
def main():
    a=hanoi(int(input()))
    print(len(a))
    print('\n'.join(a))

main()