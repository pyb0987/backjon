def creation(num):
    result = 0
    for i in range(max(1, num-len(str(num))*9), num):
        if i+sum(list(map(int, list(str(i)))))==num:
            result = i
            break
    return result
 
def main():
    num = int(input())
    print(creation(num))

main()