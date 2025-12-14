"""
@brief 贪心
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    arr = [tuple(map(int, data[i].split())) for i in range(1, m+1)]
    
    total, max_cost = 0, 0
    for i in range(m):
        a, b = arr[i]
        current = 0 if a > b else (b - a) // 2 + 1
        total += current
        max_cost = max(max_cost, current)
    
    result = total - max_cost
    print(result)

if __name__ == "__main__":
    main()