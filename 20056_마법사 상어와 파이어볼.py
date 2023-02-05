import sys
input = sys.stdin.readline 

N, M, K = map(int, input().split())
fireball = []
ground = [[[] for _ in range(N)] for _ in range(N)]
# 각 방향별 x,y 변화
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# M개의 파이어볼 정보 저장
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1,c-1,m,s,d])
    
# K번 이동
for _ in range(K):
    # 모든 파이어볼 옮기기
    while fireball:
        pr, pc, pm, ps, pd = fireball.pop()
        # 이동할 위치
        nr = (pr + ps*dr[pd]) % N # 0번행과 N-1번 행이 연결되어 있음 
        nc = (pc + ps*dc[pd]) % N
        ground[nr][nc].append([pm, ps, pd])
    
    # ground 모든 칸에 대해 탐색
    for r in range(N):
        for c in range(N):
            # 2개 이상의 fireball이 모인 경우
            if len(ground[r][c]) > 1:
                len_fb = len(ground[r][c]) # 파이어볼 개수
                m_sum, s_sum = 0, 0
                d_odd, d_even = 0, 0
                while ground[r][c]:
                    tm, ts, td = ground[r][c].pop()
                    m_sum += tm
                    s_sum += ts 
                    if td % 2: # 홀수 
                        d_odd += 1
                    else:
                        d_even += 1
                # 모두 홀수이거나 모두 짝수라면
                if d_odd == len_fb or d_even == len_fb:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                    
                if m_sum//5: # 질량이 0인 파이어볼은 소멸 -> 0이 아닌 애들만 파이어볼 살려서 추가
                    for dd in nd:
                        fireball.append([r, c, m_sum//5, s_sum//len_fb, dd])
            
            # 1개의 fireball이 모인 경우
            if len(ground[r][c]) == 1:
                fireball.append([r, c] + ground[r][c].pop())
                
print(sum([f[2] for f in fireball]))
                    
                    