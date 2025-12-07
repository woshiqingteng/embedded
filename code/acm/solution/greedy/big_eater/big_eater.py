""" 
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    N, M = list(map(int, data[0].split()))
    values = list(map(int, data[1].split()))
    
    # solve
    total = sum(values)
    if total >= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()