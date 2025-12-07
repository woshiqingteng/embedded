""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    b = list(map(int, data[2].split()))
    
    max_len = 1
    current = 1
    for i in range(n-1):
        if a[i + 1] - a[i] == b[i + 1] - b[i]:
            current += 1
            max_len = max(max_len, current)
        else:
            current = 0

    # output
    print(max_len)

if __name__ == "__main__":
    main()