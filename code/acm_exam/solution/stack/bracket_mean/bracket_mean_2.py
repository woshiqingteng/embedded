"""
@brief 暴力枚举

思路：
    枚举所有可能性，使用栈计算每种可能括号数
"""

import sys

def valid_pair(s):
    stack = []
    count = 0
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack:
                stack.pop()
                count += 1
    return count

def match_count(s):
    positions = [i for i, c in enumerate(s) if c == "?"]
    total = 0
    arrange = 1 << len(positions)

    for mask in range(arrange):
        chars = list(s)
        for i, pos in enumerate(positions):
            chars[pos] = "(" if (mask >> i) & 1 else ")"
        total += valid_pair("".join(chars))

    return total / arrange

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [data[i].strip() for i in range(1, n+1)]
    
    for s in a:
        result = match_count(s)
        print(f"{result:.4f}")

if __name__ == "__main__":
    main()