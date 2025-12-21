"""
@brief 数论

思路：
    最大公约数 * 非零长度
"""

import sys
import math
from functools import reduce

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    a = [x for x in arr if x > 0]
    g = reduce(math.gcd, a) if a else 0

    result = len(a) * g
    print(result)

if __name__ == "__main__":
    main()