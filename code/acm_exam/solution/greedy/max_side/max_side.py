"""
@brief 贪心

思路：
    数组倒序，遍历数组，元素大于等于索引+1，计数 +1
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    a.sort(reverse=True)
    count = 0

    for i in range(n):
        if a[i] >= i + 1:
            count = i + 1
        else:
            break
    
    print(count)

if __name__ == "__main__":
    main()