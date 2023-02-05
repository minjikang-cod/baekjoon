import sys
input = sys.stdin.readline

counts = []
for i in range(int(input())):
    count = 0
    temp = 0
    nA, nB = map(int, input().split())
    A = sorted(list(set(list(map(int,input().split())))), reverse=True)
    B = sorted(list(set(list(map(int,input().split())))), reverse = True)
    
    for a in A:
        while temp != len(B):
            if a>B[temp]:
                count += len(B)-temp
                break
            else:
                temp += 1

    counts.append(count)

for c in counts:
    print(c)