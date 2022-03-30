def blackj(card, sumup, cnt):
    result = [x+y+z for x in cnt for y in cnt for z in cnt if x!=y and x!=z and y!=z and x+y+z<=sumup]
    return max(result)
 
def main():
    card, sumup = tuple(map(int, input().split()))
    cnt = tuple(map(int, input().split()))
    print(blackj(card, sumup, cnt))

main()