"""
@brief 贪心

思路：
    数组正序，遍历数组，分情况进行计数
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    a.sort()
    count = 0
    i = 0
    while i < n:
        if i + 2 < n and a[i + 2] - a[i] < 10:
            count += 1
            i += 3
        elif i + 1 < n and a[i + 1] - a[i] < 20:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    
    print(count)

if __name__ == "__main__":
    main()