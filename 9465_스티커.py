import sys 
input = sys.stdin.readline 

def dp(sticker):
    for j in range(1,n): # col
        for i in range(2): # row
            if j == 1:
                sticker[i][j] += sticker[(i+1)%2][j-1]
            else:
                sticker[i][j] += max(sticker[(i+1)%2][j-1], sticker[(i+1)%2][j-2]) # 다른 행의 전 열과 전전 열과의 비교
    return max(sticker[0][n-1], sticker[1][n-1])


for _ in range(int(input())): # test case
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    print(dp(sticker))
    




'''
50 10 100 20 40
30 50 70 10 60

50 40   200  120 250
30 100  120  210 260


'''