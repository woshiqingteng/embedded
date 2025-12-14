"""
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    
    result = []
    count0 = 0 
    count1 = 0
    for char in s:
        if char == '0':
            result.append(count1)
            count0 += 1
        else:
            result.append(count0)
            count1 += 1
    
    print(*result)

if __name__ == "__main__":
    main()