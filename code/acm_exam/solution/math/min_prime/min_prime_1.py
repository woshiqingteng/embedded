"""
@brief 内置函数

思路：
    最大公约数求最小质因数
"""

import math
from functools import reduce

def min_prime(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n

def main():
    array = list(map(int, input().split()))

    gcd = reduce(math.gcd, array)
    if gcd == 1:
        print(-1)
    else:
        print(min_prime(gcd))

if __name__ == "__main__":
    main()