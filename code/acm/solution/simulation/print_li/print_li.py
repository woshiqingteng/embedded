""" 
@brief 模拟
"""

def print_li(n):
    template = [
        "...........",  # 第0行
        "..*******..",  # 第1行
        "..*..*..*..",  # 第2行
        "..*******..",  # 第3行
        "..*..*..*..",  # 第4行
        "..*******..",  # 第5行
        ".....*.....",  # 第6行
        "..*******..",  # 第7行
        ".....*.....",  # 第8行
        ".*********.",  # 第9行
        "..........."   # 第10行
    ]
    result = []
    for line in template:
        expanded_line = "".join(char * n for char in line)
        for _ in range(n):
            result.append(expanded_line)
    
    return result

def main():
    # input
    n = int(input())

    output = print_li(n)
    for line in output:
        print(line)

if __name__ == "__main__":
    main()