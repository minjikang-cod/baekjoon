import sys
input = sys.stdin.readlines

num_list = list(map(int, input()[1].split()))
LIS_list = [num_list[0]]

#이분탐색으로 풀기 - LIS를 구성하는 요소는 다르지만 LIS 길이는 같다!!!!!!!
def findLIS_BS():
    for num in num_list:
        if LIS_list[-1]<num: # 현재 lis 리스트에 있는 마지막 수보다 크면 그냥 넣기
            LIS_list.append(num)
        else: # 작거나 같으면 넣을 위치 lis 리스트에 대해 이분탐색으로 찾기
            start, end = 0, len(LIS_list)-1
            while start <= end:
                mid = (start+end)//2
                if LIS_list[mid] == num: # 같으면 바로 그 자리
                    start = mid; break
                if LIS_list[mid] < num: # 작으면 더 큰 자리 찾기
                    start = mid+1
                else: # 크면 더 작은 자리 찾기 
                    end = mid-1
            LIS_list[start] = num
    
    print(len(LIS_list))
    
findLIS_BS()