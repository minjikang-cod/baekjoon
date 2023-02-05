import sys 
input = sys.stdin.readline 

def fib(n):
    num_list = [0,1,1]
    for i in range(3,n+1):
        num_list.append(num_list[i-1] + num_list[i-2])
    return num_list[n]

def fibonacci(n):
    return n-2

if __name__ == "__main__":
    num = int(input())
    count_a = fib(num)
    count_b = fibonacci(num)
    print(count_a, count_b)