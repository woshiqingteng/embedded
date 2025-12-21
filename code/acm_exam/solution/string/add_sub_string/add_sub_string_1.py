""" 
@brief 枚举

思路：
    枚举每个可能的子串，每个可能子串从0-9遍历，并更新最小操作数
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = list(map(int, data[0].split()))
    a = data[1].strip()
    
    min_op = float('inf')
    for i in range(n - k + 1):
        s = a[i:i+k]
        for j in range(10):
            op = 0
            for c in s:
                op += abs(int(c) - j)
            min_op= min(min_op, op)

    print(min_op)

if __name__ == "__main__":
    main()