"""
@brief 模拟

思路：
    冒泡排序模拟交换
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))

    count = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()