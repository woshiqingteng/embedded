""" 
@brief 贪心

思路：
    价格升序排列，从最低价格开始遍历，直到花完钱
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = list(map(int, data[0].split()))
    a = [tuple(map(int, data[i].split())) for i in range(1, n+1)]
    
    a.sort(key=lambda x: x[1])
    amount = 0
    remain = k
    for count, price in a:
        if remain <= 0:
            break
        max_buy = min(count, remain // price)
        amount += max_buy
        remain -= max_buy * price
        
    print(amount)

if __name__ == "__main__":
    main()