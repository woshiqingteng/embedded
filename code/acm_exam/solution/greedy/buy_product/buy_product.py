"""
@brief 贪心

思路：
    数组按价格升序，遍历数组计算最小总价
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    a = [tuple(map(int, data[i].split())) for i in range(1, n+1)]

    a.sort(key=lambda x: x[0])
    money = 0
    remain = m
    for price, count in a:
        if remain <= 0:
            break
        buy = min(count, remain)
        money += buy * price
        remain -= buy
    
    print(money)

if __name__ == "__main__":
    main()