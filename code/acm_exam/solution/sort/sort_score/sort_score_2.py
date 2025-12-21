""" 
@brief 手动构造

思路：
    手动构造
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, n+1)]

    def compare_key(frac):
        a, b = frac
        if b == 0:
            return float('inf') if a > 0 else float('-inf')
        return a / b
    
    result = sorted(a, key=compare_key)

    for x, y in result:
        print(x, y)

if __name__ == "__main__":
    main()