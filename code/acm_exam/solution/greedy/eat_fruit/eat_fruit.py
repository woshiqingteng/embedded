"""
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, L = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    a.sort()
    for h in a:
        if L < h:
            break
        L += 1
    
    # output
    print(L)

if __name__ == "__main__":
    main()