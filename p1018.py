def chessboard(n,m, chess):
    savenum = 64
    for i in range(n-7):
        breakcount=0
        for j in range(m-7):
            count, count2 = 0, 0
            a = 'WBWBWBWB'
            for ii in range(0, 8, 2):
                for jj in range(8):
                    if a[jj]!=chess[i+ii][j+jj]:
                        count+=1
                    if a[7-jj]!=chess[i+1+ii][j+jj]:
                        count+=1
                    if a[7-jj]!=chess[i+ii][j+jj]:
                        count2+=1
                    if a[jj]!=chess[i+1+ii][j+jj]:
                        count2+=1
            if count==0 or count2==0:
                savenum = 0
                breakcount=1
                break
            if savenum > min(count, count2):
                savenum=min(count, count2)
            
        if breakcount==1:
            break  
    print(savenum)      


def main():
    n, m = tuple(map(int, input().split()))
    chess = []
    for i in range(n):
        chess.append(input())
    chessboard(n, m, chess)

main()