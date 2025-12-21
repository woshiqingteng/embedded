"""
@brief 栈

思路：
    左括号：入栈
    右括号：栈为空，计数+1；栈不为空，弹出栈顶，如果不匹配，计数+1
    栈中剩余左括号没有匹配，计数+len(stack)//2
"""

import sys

def adjust_count(s):
    stack = []
    count = 0
    bracket = {"(": ")", "{": "}", "[": "]"}

    for c in s:
        if c in bracket:
            stack.append(c)
        else:
            if not stack:
                count += 1
            else:
                top = stack.pop()
                if bracket[top] != c:
                    count += 1
        
    count += len(stack) // 2

    return count

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [data[i].strip() for i in range(1, n+1)]

    for s in a:
        if len(s) % 2 == 1:
            print(-1)
        else:
            print(adjust_count(s))

if __name__ == "__main__":
    main()