"""
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(float, data[2].split()))
    
    # initial
    total = 0.0
    a.sort(reverse=True)
    b.sort()
    
    # traverse
    for i in range(n):
        total += a[i] * b[i]
        
    # output
    print(f"{total:.3f}")

if __name__ == "__main__":
    main()