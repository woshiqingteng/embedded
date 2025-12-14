""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    s = data[2].strip()
    
    red = 0
    black = 0
    
    for i in range(n):
        if s[i] == 'R':
            red += a[i]
        else:
            black += a[i]
    
    total = red * black

    print(total)

if __name__ == "__main__":
    main()