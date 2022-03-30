def buljib(n):
    reach=1
    rd = 0
    while n>1:
        reach+=1
        rd+=6
        n-=rd
    print(reach)

buljib(int(input()))