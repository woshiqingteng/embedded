"""
@brief 贪心

思路：
    分别对 0 和 1 计数，交错添加结果
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    
    result = []
    count0 = 0 
    count1 = 0
    for c in s:
        if c == "0":
            result.append(count1)
            count0 += 1
        else:
            result.append(count0)
            count1 += 1
    
    print(*result)

if __name__ == "__main__":
    main()