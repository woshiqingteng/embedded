""" 
@brief 数学

思路：
    单条对角线交点数：a + b + 1 - gcd(a, b)
    两条对角线的共享交点：a 或 b 为偶数
"""

import math

def main():
    a, b, x, y = map(int, input().split())

    line = a + b + 1 - math.gcd(a, b)
    total = 2 * line
    if a % 2 == 0 or b % 2 == 0:
        total -= 1

    print(total)

if __name__ == "__main__":
    main()