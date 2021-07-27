# Uses python3
import sys

def lcm_improved(a, b):
    list_a = []
    list_b = []
    for x in range(1, 10):
        list_a.append(a * x) 
        list_b.append(b * x)

    if min(set(list_a).intersection(set(list_b)), default="EMPTY") == "EMPTY":
        return a*b
    else:
        return min(set(list_a).intersection(set(list_b)))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_improved(a, b))

