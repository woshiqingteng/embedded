"""
@brief 栈

思路：
    左括号：入栈
    右括号：栈为空，返回 False；栈不为空，弹出栈顶，如果不匹配，返回 False
    栈中剩余左括号没有匹配，返回 False
"""

import sys

def is_valid(s):
    stack = []
    bracket = {"(": ")", "{": "}", "[": "]"}
    
    for c in s:
        if c in bracket:
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if bracket[top] != c:
                    return False
    
    return not stack

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [data[i].strip() for i in range(1, n+1)]
    
    for s in a:
        print(is_valid(s))

if __name__ == "__main__":
    main()