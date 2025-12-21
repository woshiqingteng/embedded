"""
@brief 数论

思路：
    比较小写字母和 k 大小，计算结果
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = str(data[1].strip())
    
    upper = sum(1 for c in s if c.isupper())
    lower = n - upper
    if k <= lower:
        result = upper + k
    else:
        result = n - ((k - lower) % 2)
    
    print(result)

if __name__ == "__main__":
    main()