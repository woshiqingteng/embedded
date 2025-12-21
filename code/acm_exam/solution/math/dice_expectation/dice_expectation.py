"""
@brief 数学
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, x, y = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    px = a.count(x) / n
    py = a.count(y) / n
    result = 1.0 / (px * py)

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()