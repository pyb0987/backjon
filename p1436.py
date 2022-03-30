def movie666(num):
    result = [666, 1666, 2666, 3666, 4666, 5666]
    n=6600
    while True:
        test = str(n)
        if test.count('6')>=3:
            if '666' in test:
                result.append(int(n))
                if len(result)>=num:
                    break
        n+=1
    return result[num-1]
 

print(movie666(int(input())))