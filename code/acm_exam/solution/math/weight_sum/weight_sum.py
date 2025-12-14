"""
@brief 数学
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    arr = list(map(int, data[0].split()))

    result = max(arr) - min(arr)
    
    print(result)

if __name__ == "__main__":
    main()