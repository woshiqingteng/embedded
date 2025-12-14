"""
@brief 排序
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    arr.sort()
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()