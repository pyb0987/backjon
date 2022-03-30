def main():
    import sys
    n = int(input())
    inp = list(map(int, sys.stdin.readline().rstrip().split()))
    inpkey = sorted(set(inp))
    i = 0
    ord_dict = {}
    for key in inpkey:
        ord_dict[key] = str(i)
        i+=1
    print(' '.join([ord_dict[inp_elem] for inp_elem in inp]))

main()