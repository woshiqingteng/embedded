"""
@brief 贪心
"""

def calculate(expr):
    result = 0
    current_num = 0
    sign = 1  # 1表示正，-1表示负
    has_digit = False
    
    for ch in expr + '+':  # 加'+'方便处理最后一个数字
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
            has_digit = True
        else:  # 运算符
            if has_digit:
                result += sign * current_num
                current_num = 0
                has_digit = False
                sign = 1 if ch == '+' else -1
    
    return result

def main():
    # input
    s = str(input().strip())
    n = len(s)

    max_result = float('-inf')
    
    for i in range(n):
        string = s[:i] + s[i+1:]
        result = calculate(string)
        max_result = max(max_result, result)

    print(max_result)

if __name__ == "__main__":
    main()