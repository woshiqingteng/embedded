""" 
@brief 栈计数

思路：
    左括号：索引入栈
    右括号：栈不为空出栈，栈再不为空，更新前缀长度为该字符索引+1
"""

import sys

def valid_prefix(s):
    stack = []
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if not stack:
                break
            else:
                stack.pop()
                if not stack:
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