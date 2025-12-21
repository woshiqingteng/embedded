"""
@brief 栈

思路：
    "a"：入栈
    "b"：栈为空，返回 False；栈不为空，弹出栈顶，如果不匹配，返回 False
    栈中剩余 "a" 没有匹配，返回 False
"""

def is_valid(s):
    stack = []
    
    for c in s:
        if c == "a":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
                if "b" != c:
                    return False
    
    return not stack

def main():
    s = input().strip()

    result = "YES" if is_valid(s) else "NO"

    print(result)

if __name__ == "__main__":
    main()