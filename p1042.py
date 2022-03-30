def lier(ppl, partynum, truth, schedule):
    truth.pop(0)
    truth = set(truth)
    while len(truth)>0:
        truth_to_be = set()
        schedule_to_be = []
        for party in schedule:
            if truth & set(party[1:])!=set():
                truth_to_be = (truth_to_be | set(party[1:]))-set(truth)
            else:
                schedule_to_be.append(party)
        schedule = schedule_to_be
        truth = truth_to_be
    print(len(schedule))

def main():
    ppl, partynum = map(int, input().split())
    truth = list(map(int, input().split()))
    inp = []
    for _ in range(partynum):
        inp.append(tuple(map(int,input().split())))
    lier(ppl, partynum, truth, inp)

main()



    