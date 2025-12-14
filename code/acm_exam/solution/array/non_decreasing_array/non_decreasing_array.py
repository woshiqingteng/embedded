"""
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    count = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            count += a[i-1] - a[i]
            a[i] = a[i-1]
    
    print(count)

if __name__ == "__main__":
    main()