# Uses python3
import sys

def fibonacci_partial_sum_improved(from_, to):
    if to == 0:
        return 0
    else:
        fib_list = [0,1]
        for x in range(0,to-1):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return sum(fib_list[from_:])%10    


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_improved(from_, to))