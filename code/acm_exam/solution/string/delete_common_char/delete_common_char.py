"""
@brief 字符串

思路：
    条件遍历
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    a = data[0].strip()
    b = data[1].strip()
        
    result = "".join([c for c in a if c not in b])
    print(result)

if __name__ == "__main__":
    main()