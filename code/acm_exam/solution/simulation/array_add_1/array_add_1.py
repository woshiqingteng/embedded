"""
@brief 模拟

思路：
    遍历输入区间，并更新结果数组
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, t = map(int, data[0].split())
    a = [list(map(int, data[i].split())) for i in range(1, t+1)]
    
    reuslt = [0] * n
    for l, r, v in a:
        start = v * ((l + v - 1) // v)
        for j in range(start, r + 1, v):
            reuslt[j-1] += 1

    print(*reuslt)

if __name__ == "__main__":
    main()