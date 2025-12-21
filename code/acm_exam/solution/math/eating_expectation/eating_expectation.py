"""
@brief 数学

思路：E[n] = n
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [int(data[i]) for i in range(1, n+1)]
    
    for i in range(n):
        print(a[i])

if __name__ == "__main__":
    main()