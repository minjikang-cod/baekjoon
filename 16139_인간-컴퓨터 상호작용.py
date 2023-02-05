import sys
input = sys.stdin.readline

sentence = input().rstrip() 
#words = {}
#
#for _ in range(int(input())):
#    i = input().split()
#    # 나온 적 없다면
#    if i[0] not in words:
#        # 첫 단어가 알파벳과 동일하다면 1로 시작 아니라면 0으로 시작
#        words[i[0]] = [1] if sentence[0] == i[0] else [0]
#        for j in range(1, len(sentence)):
#            words[i[0]].append(words[i[0]][-1] + 1 if sentence[j] == i[0] else words[i[0]][-1])
#    
#    print(words[i[0]][int(i[2])]-words[i[0]][int(i[1])-1] if int(i[1]) else words[i[0]][int(i[2])])

words = [[0 for _ in range(26)]] # 알파벳 a-z : 26개
words[0][ord(sentence[0])-97] = 1 # 맨 처음 알파벳 개수 1로 초기화
for i in range(1, len(sentence)):
    words.append(list(words[-1]))
    words[-1][ord(sentence[i])-97] += 1

for _ in range(int(input())):
    i = input().split()
    if int(i[1]):
        print(words[int(i[2])][ord(i[0])-97]-words[int(i[1])-1][ord(i[0])-97])
    else:
        print(words[int(i[2])][ord(i[0])-97])