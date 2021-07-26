# Uses python3
import sys

def gcd_naive(a, b):
    bigger = max(a,b)
    smaller = min(a,b)
    remainder = bigger % smaller
    remainders = []
    if (remainder == 0):
            return smaller
    else:
        while remainder != 0:
            remainder = bigger % smaller
            remainders.append(smaller)
            bigger = smaller 
            smaller = remainder
        return remainders[-1]

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
