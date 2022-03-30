def yeonsan(n, list1, list2, start=0):
    global number, maxmin
    resultset = [start+list1[number-n], start-list1[number-n], start*list1[number-n], int(start/list1[number-n])]
    for i in range(4):
        if (list2[i] and n!=number):
            if n==1:
                if maxmin is not None:
                    maxmin = [max(maxmin[0], resultset[i]), min(maxmin[1], resultset[i])]
                else:
                    maxmin = [resultset[i], resultset[i]]
            else:
                yeonsan(n-1, list1, list2[:i]+[list2[i]-1]+list2[i+1:], resultset[i])
    if number==n:
        yeonsan(n-1, list1, list2, resultset[0])
    return maxmin

maxmin = None
number = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
a = yeonsan(number, list1, list2)
print(a[0], a[1], sep='\n', end='')