"""
@brief 数学
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, t = map(int, data[0].split())
    a = [list(map(int, data[i].split())) for i in range(1, t+1)]
    
    arr = [0] * (n + 1)
    for i in range(t):
        l, r, v = a[i]
        start = v * ((l + v - 1) // v)
        for j in range(start, r + 1, v):
            arr[j] += 1

    result = " ".join(map(str, arr[1:]))
    print(result)

if __name__ == "__main__":
    main()