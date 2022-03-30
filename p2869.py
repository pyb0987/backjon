def snail(tup):
    up, sleep, height = tuple(map(int, tup))
    print((height-up)//(up-sleep)+2-((height-up)%(up-sleep)==0))

snail((input().split()))
