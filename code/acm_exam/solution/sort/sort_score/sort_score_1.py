""" 
@brief 内置函数

思路：
    调用 Fraction 进行分数排序
"""

import sys
from fractions import Fraction

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, n+1)]
    
    result = sorted(a, key=lambda x: Fraction(x[0], x[1]))

    for x, y in result:
        print(x, y)

if __name__ == "__main__":
    main()