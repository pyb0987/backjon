def ts(k, tsinput):
    alphabets = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counter = {x:0 for x in alphabets}
    for word in tsinput:
        for i in range(len(word)):
            a = 35-alphabets.index(word[i])
            counter[word[i]] += a*36**(len(word)-i-1)
    choice = [i[0] for i in (sorted(counter.items(), key=lambda x : -x[1]))[:k]]
    sumup, result = 0, ""
    for word in tsinput:
        for i in range(len(word)):
            a = alphabets.index(word[i])
            if word[i] in choice:
                a=35
            sumup += a*36**(len(word)-i-1)
    if sumup ==0:
        result = '0'
    while sumup>0:
        result = alphabets[sumup%36] + result
        sumup = sumup//36
    print(result)




n = int(input())
tsinput = []
for i in range(n):
    tsinput.append(list(input()))
k = int(input())
ts(k, tsinput)
