""" 
@brief 几何

思路：分割成6个三角形计算面积
"""

import sys
import math

def main():
    data = sys.stdin.read().splitlines()
    a = list(map(float, data[0].split()))
    l = float(data[1])

    area = 0.0
    for i in range(6):
        j = (i + 1) % 6
        area += 0.5 * (a[i]*l/100) * (a[j]*l/100) * math.sin(math.pi / 3)

    print(f"{area:.6f}")

if __name__ == "__main__":
    main()