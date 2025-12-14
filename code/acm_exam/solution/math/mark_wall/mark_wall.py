""" 
@brief 数学
"""

import math

def main():
    data = input().split()
    a, b, x, y = map(int, data)
    d = math.gcd(a, b)
    line_points = a + b + 1 - d
    total_points = 2 * line_points
    if a % 2 == 0 or b % 2 == 0:
        total_points -= 1
    print(total_points)

if __name__ == '__main__':
    main()