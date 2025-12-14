""" 
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))
    
    # solve
    arr.sort()
    if 2 * k <= n:
        t = k
    else:
        t = n - k
    
    result = sum(arr[-t:]) - sum(arr[:t])
    
    # output
    print(result)

if __name__ == "__main__":
    main()