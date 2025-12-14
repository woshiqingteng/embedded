""" 
@brief 冒泡排序
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m = list(map(int, data[0].split()))
    a = list(map(int, data[1].split()))
    
    # solve
    for k in range(1, m + 1):
        for i in range(n - 1):
            if a[i] % k > a[i + 1] % k:
                a[i], a[i + 1] = a[i + 1], a[i]
    
    # output
    print(" ".join(map(str, a)))

if __name__ == "__main__":
    main()