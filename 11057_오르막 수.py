N = int(input())

def dp(N):
    num_list = [1]*10
    for _ in range(N-1):
        temp = [sum(num_list)]
        for j in range(9):
            temp.append(temp[-1]-num_list[j])
        num_list = temp 
    
    return sum(num_list)

def dp2(N): # 앞 식을 거꾸로 적용해서 더 간단하게 정리하기    
    num_list = [1]*10
    for _ in range(N-1):
        for j in range(1,10):
            num_list[j] += num_list[j-1]
    
    return sum(num_list)
    
print(dp(N)%10007)
print(dp2(N)%10007)




'''
1 1 1 1 1 1 1 1 1 1
10 9 8 7 6 5 4 3 2 1
55 45 36 28 21 15 10 6 3 1
220 

1   2   3

10  55  

0 - 0 - 10
0 - 1 - 9
...
55

1 - 1 - 9
1 - 2 - 8

45

36
'''