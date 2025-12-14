""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))
    if sum(a) != sum(b):
        print(-1)
        return
    
    # solve
    total = 0
    for i in range(n):
        total += max(b[i] - a[i], 0)
    
    # output
    print(total)

if __name__ == "__main__":
    main()