"""
@brief 贪心

思路：
    数组正序排序，从低遍历数组，蛇长度大于当前元素，蛇长度 +1，否则中断
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, l = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    a.sort()
    for h in a:
        if l >= h:
            l += 1
        else:
            break

    print(l)

if __name__ == "__main__":
    main()