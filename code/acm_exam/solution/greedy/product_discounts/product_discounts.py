"""
@brief 贪心

思路：
    对商品价格（降序）和折扣（升序）进行排序，折扣 * 数量，求和
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(float, data[1].split()))
    b = list(map(float, data[2].split()))
    
    total = 0.0
    a.sort(reverse=True)
    b.sort()
    for i in range(n):
        total += a[i] * b[i]

    print(f"{total:.3f}")

if __name__ == "__main__":
    main()