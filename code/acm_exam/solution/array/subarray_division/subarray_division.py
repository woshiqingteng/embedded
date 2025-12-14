"""
@brief 数组
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    for i in range(k - 1, n):
        a = prefix[n] - prefix[i]
        for j in range(max(k - 2, 0), i):
            if k == 2 and j != 0: 
                continue
            b = prefix[i] - prefix[j]
            if b != 0 and a % b == 0:
                print("Yes")
                return
    
    print("No")

if __name__ == "__main__":
    main()