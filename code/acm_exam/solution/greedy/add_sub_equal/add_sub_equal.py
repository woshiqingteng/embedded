""" 
@brief 贪心

思路：
    a 的和不等于 b 的和，返回 -1
    遍历，b[i] > a[i]，求 b[i] - a[i] 的和
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))

    if sum(a) != sum(b):
        print(-1)
        return
    total = 0
    for i in range(n):
        total += max(b[i] - a[i], 0)
    
    print(total)

if __name__ == "__main__":
    main()