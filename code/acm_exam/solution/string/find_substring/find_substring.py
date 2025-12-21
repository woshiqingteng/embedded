"""
@brief 字符串匹配

思路：
    构造匹配计数函数，遍历每一个字符串
"""

import sys

def s_count(text, pattern):
    count = 0
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = data[1].strip()
    b = [data[i].strip() for i in range(2, n+2)]
    
    total = 0
    for c in b:
        total += s_count(a, c)
    
    print(total)

if __name__ == "__main__":
    main()