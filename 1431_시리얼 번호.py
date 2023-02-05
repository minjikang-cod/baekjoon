import sys
input = sys.stdin.readline

def sumnum(str):
    only_num = [ int(s) for s in list(str) if s.isdigit() ]
    return sum(only_num)

if __name__ == "__main__":
    N = int(input())
    serial_list = [input().rstrip() for _ in range(N)]
    serial_list.sort(key = lambda x : (len(x),sumnum(x),x))
    
    print('\n'.join(serial_list))