"""
@brief 字符串
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    a = data[0].strip()
    b = data[1].strip()
        
    result = ''.join([ch for ch in a if ch not in b])
    print(result)

if __name__ == "__main__":
    main()