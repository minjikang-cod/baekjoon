def count_people (k, n):
    people = 0
    if n == 0:
        people = 0
    elif k == 0:
        people = n
    else:
        people = count_people(k-1,n) + count_people(k, n-1)
    
    return people

if __name__ == "__main__":
    case = int(input())
    total_list = []
    for c in range(case):
        k = int(input())
        n = int(input())
        
        total_list.append(count_people(k,n))
    
    for t in total_list:
        print(t)
        