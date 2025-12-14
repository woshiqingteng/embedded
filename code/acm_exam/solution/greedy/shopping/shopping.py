"""
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    a = [tuple(map(int, data[i].split())) for i in range(1, n+1)]

    a.sort(key=lambda x: x[0])
    total = 0
    remain = m
    
    for price, count in a:
        if remain <= 0:
            break
        buy = min(count, remain)
        total += buy * price
        remain -= buy
    
    # output
    print(total)

if __name__ == "__main__":
    main()