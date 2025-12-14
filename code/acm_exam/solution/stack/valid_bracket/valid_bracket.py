"""
@brief 栈
"""

import sys

def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    
    return not stack

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = [data[i].strip() for i in range(1, n+1)]
    
    # output
    for string in s:
        result = is_valid(string)
        print(str(result))

if __name__ == "__main__":
    main()
