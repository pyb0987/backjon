a, b = map(int, input().split())
yesyes = []
for prime in range(2, int(b**0.5)+1):    
    for k in range(((a-1)//prime**2)+1, (b//prime**2)+1):
        yesyes.append(k*prime**2)
yesyes = sorted(list(set(yesyes)))
print(b-a+1-len(yesyes))
