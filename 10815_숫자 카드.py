N = int(input())
card = input()
card_list = list(map(lambda x : int(x),card.split(' ')))
card_list.sort()

M = int(input())
integer = input()
integer_list = list(map(lambda x : int(x), integer.split(' ')))

answer = [0 for _ in range(M)]

for i in range(M):
    start = 0
    end = N-1 
    while end >= start:
        mid = int((start+end)/2)
        
        if integer_list[i] == card_list[mid]:
            answer[i] = 1
            break
        elif integer_list[i] > card_list[mid]:
            start = mid+1
        elif integer_list[i] < card_list[mid]:
            end = mid-1


print(' '.join([str(_) for _ in answer]))