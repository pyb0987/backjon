def main():
    import sys
    n= int(input())
    inp = [[] for _ in range(51)]
    for i in range(n):
        tmp = sys.stdin.readline().rstrip()
        inp[len(tmp)].append(tmp)
    
    for words in inp:
        if words!=[]:
            print('\n'.join(sorted(set(words))))

main()