"""
@brief 数学
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    day = [int(data[i]) for i in range(1, n+1)]
    
    # solve
    for i in range(n):
        print(day[i])

if __name__ == "__main__":
    main()