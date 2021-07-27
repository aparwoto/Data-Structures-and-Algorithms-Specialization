# Uses python3
from sys import stdin

def fibonacci_sum_squares_improved(n):
    if n == 0:
        return 0
    else:
        fib_list = [0,1]
        for x in range(0,n-1):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return sum(list(map(lambda x: x**2,fib_list)))%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_improved(n))
