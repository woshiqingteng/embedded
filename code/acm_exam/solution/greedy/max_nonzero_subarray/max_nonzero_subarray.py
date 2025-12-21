""" 
@brief 贪心

思路：
    遍历数组，非零计数 +1，并更新最大长度
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    max_len = 0
    count = 0
    for x in a:
        if x != 0:
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0
    
    print(max_len)

if __name__ == "__main__":
    main()