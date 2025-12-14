"""
@brief 数学
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, X, Y = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    px = a.count(X) / n
    py = a.count(Y) / n
    result = 1.0 / (px * py)
    
    # output
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()