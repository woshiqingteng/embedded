""" 
@brief 模拟

思路：
    根据 n = 1 的每行模板，每行单个字符串重复 n 次，行数重复 n 次
"""

def print_li(n):
    template = [
        "...........",
        "..*******..",
        "..*..*..*..",
        "..*******..",
        "..*..*..*..",
        "..*******..",
        ".....*.....",
        "..*******..",
        ".....*.....",
        ".*********.",
        "..........." 
    ]
    result = []
    for line in template:
        new_line = "".join(c * n for c in line)
        for _ in range(n):
            result.append(new_line)
    
    return result

def main():
    n = int(input())

    output = print_li(n)
    for line in output:
        print(line)

if __name__ == "__main__":
    main()