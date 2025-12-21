"""
@brief 统计

思路：
    集合去重
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    am = [list(map(int, data[i].split())) for i in range(1, m+1)]
    
    bless = [0] * n
    for j in range(m):
        avg = sum(am[j]) / n
        for i in range(n):
            if am[j][i] > avg:
                bless[i] = 1
    result = sum(bless)
    
    print(result)

if __name__ == "__main__":
    main()