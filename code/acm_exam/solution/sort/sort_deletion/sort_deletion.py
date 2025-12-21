"""
@brief 数论

思路：
    遍历数组，相邻差值大于1返回错误
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    a.sort()
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()