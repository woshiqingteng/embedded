""" 
@brief 字符串
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    a = data[0]
    b = data[1]
    
    # solve
    mid = len(b) // 2
    
    # output
    print(a+b[mid:])
    print(b[:mid])

if __name__ == "__main__":
    main()