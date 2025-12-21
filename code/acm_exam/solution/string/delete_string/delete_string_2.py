"""
@brief 手动构造

思路：
    字符串末尾添加 "+"
    从头遍历字符串，遇到数字，自计数，其他情况，根据符号位累加，重置符号位、数字标志、计数
"""

def calculate(s):
    result = 0
    current = 0
    sign = 1
    has_digit = False
    
    for c in s:
        if c.isdigit():
            current = current * 10 + int(c)
            has_digit = True
        else:
            if has_digit:
                result += sign * current
                current = 0
                has_digit = False
                sign = 1 if c == "+" else -1
    
    return result

def main():
    s = input().strip()

    n = len(s)
    max_result = float('-inf')
    
    for i in range(n):
        string = s[:i] + s[i+1:]
        result = calculate(string)
        max_result = max(max_result, result)

    print(max_result)

if __name__ == "__main__":
    main()