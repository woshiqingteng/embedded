"""
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m, a, b = map(int, data[0].split())
    
    count = n // m
    remain = n % m
    cycle = min(a+m, m*(b+1))
    if remain > 0:
        remain = min(a+remain, remain*(b+1))
    else:
        remain = 0
    
    total = count * cycle + remain
    print(total)

if __name__ == "__main__":
    main()