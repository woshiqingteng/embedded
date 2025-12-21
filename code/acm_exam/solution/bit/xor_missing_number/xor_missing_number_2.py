""" 
@brief 普通异或

思路：
    缺失数 xor(n) ^ k 
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, t+1)]

    for i in range(t):
        n, k = a[i]
        total_xor = 0
        for j in range(1, n + 1):
            total_xor ^= j
        missing = total_xor ^ k
      
        print(missing)

if __name__ == "__main__":
    main()