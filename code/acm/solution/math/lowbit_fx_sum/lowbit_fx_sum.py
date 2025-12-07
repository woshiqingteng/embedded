""" 
@brief 位运算
"""

import sys

def main():
    # read
    n = int(sys.stdin.readline().strip())
    
    # solve
    total = 0
    for i in range(1, n + 1):
        fx = i & -i
        total += i // fx
    
    print(total)

if __name__ == "__main__":
    main()