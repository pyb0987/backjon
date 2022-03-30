def bunsu(n):
    point = 1
    space = 1
    while(n-space>=point) :
        point+=space
        space+=1
    if space%2:
        print(str(space-n+point)+'/'+str(n-point+1))
    else:
        print(str(n-point+1)+'/'+str(space-n+point))

bunsu(int(input()))