"""
@brief 贪心

思路：
    遍历数组，累加操作数并更新最大操作数，结果为操作数累加和减最大操作数
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    am = [tuple(map(int, data[i].split())) for i in range(1, m+1)]
    
    total, max_cost = 0, 0
    for a, b in am:
        count = 0 if a > b else (b - a) // 2 + 1
        total += count
        max_cost = max(max_cost, count)
    
    result = total - max_cost
    print(result)

if __name__ == "__main__":
    main()