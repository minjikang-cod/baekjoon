import sys

inp = sys.stdin.readline
n,m = map(int, inp().split())
chess = []
color_change = []

for i in range(n):
    chess.append(list(inp()[:-1]))

for j in range(n-7):
    for k in range(m-7):
        count = 0
        chess_88 = chess[j:j+8][k:k+8]
        for j8 in range(8):
            for k8 in range(8):
                main = chess_88[j8][k8]
                if k8 >= 1: left = chess_88[j8][k8-1]
                else: left = 'O'
                right = chess_88[j8][k8+1]
                up = chess_88[j8-1][k8]
                down = chess_88[j8+1][k8]
                if main == left or main == right or main == up or main == down:
                    count = count+1
        color_change.append(count)

print(min(color_change))