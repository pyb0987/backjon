import sys
import itertools
def w(ntuple):
    hyperlib = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    sumnum = {}
    comb = list(itertools.combinations_with_replacement(range(21), 3))
    for k, g in itertools.groupby(comb, lambda x : x[0]+x[1]+x[2]):
        sumnum[k] = sumnum.get(k, []) + [x for x in list(g)]

    for i in range(0, 61):
        for eachcom in sumnum[i]:
            for a, b, c in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
                if min(eachcom[a], eachcom[b], eachcom[c])==0:
                    hyperlib[eachcom[a]][eachcom[b]][eachcom[c]] = 1
                elif eachcom[a]<eachcom[b] and eachcom[b]<eachcom[c]:
                    hyperlib[eachcom[a]][eachcom[b]][eachcom[c]] = hyperlib[eachcom[a]][eachcom[b]][eachcom[c]-1]+hyperlib[eachcom[a]][eachcom[b]-1][eachcom[c]-1]-hyperlib[eachcom[a]][eachcom[b]-1][eachcom[c]]
                else:
                    hyperlib[eachcom[a]][eachcom[b]][eachcom[c]] = hyperlib[eachcom[a]-1][eachcom[b]][eachcom[c]]+hyperlib[eachcom[a]-1][eachcom[b]-1][eachcom[c]]+hyperlib[eachcom[a]-1][eachcom[b]][eachcom[c]-1]-hyperlib[eachcom[a]-1][eachcom[b]-1][eachcom[c]-1]
    for a, b, c in ntuple:
        print('w({0}, {1}, {2}) = {3}'.format(a,b,c, hyperlib[0 if min(a,b,c)<=0 else 20 if max(a,b,c)>=21 else a][0 if min(a,b,c)<=0 else 20 if max(a,b,c)>=21 else b][0 if min(a,b,c)<=0 else 20 if max(a,b,c)>=21 else c]))

inp = []
while True:
    inp.append(list(map(int, sys.stdin.readline().rstrip().split())))    
    if inp[-1] == [-1,-1,-1]:
        inp.pop()
        break
w(inp)
    