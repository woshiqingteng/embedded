"""
@brief 手动构造

思路：
    初始化每个数字出现次数
    遍历每个数字，a = k / 2，只保留1个，计数增加次数-1，其他，次数增加两个数字的最小值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    count = 0
    for x in freq:
        y = k - x
        if x == y:
            count += freq[x] - 1
        elif x < y:
            count += min(freq[x], freq.get(y, 0))
    
    print(count)

if __name__ == "__main__":
    main()