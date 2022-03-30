def sonic(a):
    if a[0]>0 and a[1]>=a[2]:
        print(-1)
    else:
        print(a[0]//(a[2]-a[1])+1)

sonic(tuple(map(int, input().split())))