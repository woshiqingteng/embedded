"""
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    a.sort(reverse=True)
    count = 0

    for i in range(n):
        if a[i] >= i + 1:
            count = i + 1
        else:
            break
    
    # output
    print(count)

if __name__ == "__main__":
    main()