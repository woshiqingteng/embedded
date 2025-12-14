""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, k = list(map(int, data[0].split()))
    shop = [tuple(map(int, data[i].split())) for i in range(1, n+1)]
    
    shop.sort(key=lambda x: x[1])
    total = 0
    remain = k
    
    for count, price in shop:
        max_buy = min(count, remain // price)
        total += max_buy
        remain -= max_buy * price

        if remain <= 0:
            break
    
    print(total)

if __name__ == "__main__":
    main()