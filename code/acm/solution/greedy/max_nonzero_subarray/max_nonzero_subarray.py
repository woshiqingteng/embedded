""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    max_len = 0
    current= 0
    for num in arr:
        if num != 0:
            current += 1
            max_len = max(max_len, current)
        else:
            current = 0
    
    print(max_len)

if __name__ == "__main__":
    main()