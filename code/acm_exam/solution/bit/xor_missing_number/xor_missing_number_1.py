""" 
@brief 快速异或

思路：
    缺失数 xor(n) ^ k 
"""

import sys

def fast_xor(n):
    mod = n & 3 # mod = n % 4
    if mod == 0:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n + 1
    else:
        return 0

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, t+1)]

    for i in range(t):
        n, k = a[i]
        missing = fast_xor(n) ^ k
    
        print(missing)

if __name__ == "__main__":
    main()