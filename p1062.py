def teach(N, K, inp):
    import itertools
    if K<5:
        return 0
    else:
        basic = set(['a', 'n', 't', 'c', 'i'])
        inpset = []
        allset = set({})
        for word in inp:
            if K-5>= len(set(word)-basic):
                inpset.append(set(word)-basic)
                allset = allset | inpset[-1]
        maximum = 0
        for comb in itertools.combinations(allset, min(len(allset), K-5)):
            count = 0
            for word in inpset:
                if word<=set(comb):
                    count +=1
            maximum = max(count, maximum)
        return maximum

def main():
    import sys
    N, K = map(int, input().split())
    inp = [sys.stdin.readline().rstrip() for _ in range(N)]
    print(teach(N, K, inp))

main()
