import sys
input = sys.stdin.readlines

card_list = []
for i in input():
    card_list.append(int(i.rstrip()))
card_list = sorted(list(set(card_list)))

sum_set = set()
for i in card_list:
    for j in card_list:
        sum_set.add(i+j) # list에 받아서 정렬하고 중복제거할게 아니라 그냥 set에 받기! set은 원소 찾을 때 시간 복잡도 O(1)
card_num = len(card_list)

def check():
    for i in range(card_num-1, -1, -1):
        for j in range(0, i+1):
            if card_list[i]-card_list[j] in sum_set:
                print(card_list[i]); return

check()