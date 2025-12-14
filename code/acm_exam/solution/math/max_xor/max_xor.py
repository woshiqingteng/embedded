"""
@brief 位运算
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    a = [list(map(int, data[i].split())) for i in range(1, t+1)]
    
    for i in range(t):
        x, k = a[i]
        y = 0
        for j in range(31, -1, -1):
            x_bit = (x >> j) & 1
            desired = 1 - x_bit
            if (y | (desired << j)) <= k:
                y |= desired << j
        if y == 0:
            y = 1
        print(y)

if __name__ == "__main__":
    main()