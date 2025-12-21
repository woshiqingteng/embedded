""" 
@brief 模拟

思路：
    两数组每位数字之差取模并求和
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    a = data[0].strip()
    b = data[1].strip()

    total = 0
    for i in range(4):
        total += (int(a[i]) - int(b[i])) % 10
    
    print(total)

if __name__ == "__main__":
    main()