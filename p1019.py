def page(n, i):
    ans = 0
    bible = [0, 1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000, 1000000000]
    for j in range(0, len(n)):
        if i == int(n[j]):
            ans+=(1 if len(n)==j+1 else int(n[j+1:])+1)
        elif i <= int(n[j]):
            ans += 10**(len(n)-1-j)
        if i == 0:
            ans -= 10**(len(n)-1-j)
        ans+=int(n[j])*bible[len(n)-1-j]
    return ans

n = input()
result = []
for i in range(10):
    result.append(str(page(n, i)))
print(' '.join(result))


