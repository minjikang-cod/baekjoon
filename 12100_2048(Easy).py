import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def backtracking(board, cnt):
    global answer  
    if cnt == 5: # 5번 다 움직임
        for i in range(N):
            answer = max(answer, max(board[i]))
        return 
    
    for i in range(4): # 상하좌우
        temp_board = move([x[:] for x in board],i)
        backtracking(temp_board, cnt+1)
        

def move(board, dir): # 상하좌우 움직이는 함수
    if dir == 0: # 상 (col 그대로, row -1씩)
        for j in range(N):
            top = 0
            for i in range(1, N):
                if board[i][j]: # 블럭이 있으면
                    tmp = board[i][j]
                    board[i][j] = 0 # 해당 블럭 값 옮길거니까 빈칸으로 바꾸기
                    if board[top][j] == 0: # 맨 위에 블럭이 없으면
                        board[top][j] = tmp
                    elif board[top][j] == tmp: # 맨 위에 똑같은 블럭이 있으면 
                        board[top][j] = tmp * 2
                        top += 1
                    else: # 맨 위에 다른 블럭이 있으면
                        top += 1
                        board[top][j] = tmp # 다음 블럭에다가 옮기기
    
    elif dir == 1: # 하 (col 그대로, row +1씩)
        for j in range(N):
            top = N-1
            for i in range(N-2, -1, -1):
                if board[i][j]: # 블럭이 있으면
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp 
                    elif board[top][j] == tmp:
                        board[top][j] = tmp*2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp
                        
    elif dir == 2: # 좌 (col -1씩, row 그대로)
        for i in range(N):
            top = 0
            for j in range(1, N):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2 
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp 
    
    else: # 우 (col +1씩, row 그대로)
        for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp 
    
    return board
                    
backtracking(board, 0) 
print(answer)