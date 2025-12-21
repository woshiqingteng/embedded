""" 
@brief 直接计数

思路：
    左括号：count +1
    右括号：count -1
    count < 0 中断，count = 0 更新前缀长度为该字符索引+1
"""

import sys

def valid_prefix(s):
    count = 0
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
        elif count == 0:
            max_len = i + 1

    return max_len

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [data[i].strip() for i in range(1, n+1)]
    
    for s in a:
        print(valid_prefix(s))

if __name__ == "__main__":
    main()