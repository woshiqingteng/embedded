""" 
@brief 排序
"""

import sys
from functools import cmp_to_key

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = [tuple(map(int, data[i].split())) for i in range(1, n+1)]

    def compare(frac1, frac2):
        a, b = frac1
        c, d = frac2
        left = a * d
        right = b * c
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    
    arr.sort(key=cmp_to_key(compare))

    for i in range(n):
        print(arr[i][0], arr[i][1])

if __name__ == "__main__":
    main()