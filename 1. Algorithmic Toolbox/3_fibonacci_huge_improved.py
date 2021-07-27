# Uses python3
import sys

def get_fibonacci_huge_improved(n, m):
    if n == 0:
        return 0
    else:
        fib_list = [0,1]
        for x in range(0,n-1):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[-1]%m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_improved(n, m))
