""" 
@brief 贪心

思路：
    遍历数组，计算相邻两数之差的比较，更新最大长度
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))
    
    max_len = 1
    count = 1
    for i in range(n-1):
        if a[i + 1] - a[i] == b[i + 1] - b[i]:
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0

    print(max_len)

if __name__ == "__main__":
    main()