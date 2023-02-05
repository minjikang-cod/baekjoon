test = int(input())
num_list = []
partition = []

for _ in range(test):
    num_list.append(int(input()))

max_num = max(num_list)
is_prime = [True for _ in range(max_num+1)]
# 가장 큰 숫자까지 list 만들어서 소수 여부 구하기
for i in range(max_num+1):
    if i==0 or i==1:
        is_prime[i] = False
    else:
        if is_prime[i]== True:
            j=2
            while(i*j<=max_num):
                is_prime[i*j]=False
                j += 1
# partition의 두 수가 소수인지, 차이가 가장 작은지 확인하고 쌍 만들기
for num in num_list:
    difference = num
    for left in range(2,num+1):
        if is_prime[left]:
            right = num-left
            if not is_prime[right]:
                continue
            else:
                if difference > right-left and right-left >= 0:
                    difference = right-left
                    part = str(left) + ' ' + str(right)
                else:
                    break
                
    partition.append(part)

for p in partition:
    print(p)