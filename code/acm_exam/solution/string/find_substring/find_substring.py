"""
@brief 滑动窗口
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
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = str(data[1].strip())
    b = [str(data[i].strip()) for i in range(2, n+2)]
    
    total = 0
    for i in range(n):
        total += s_count(a, b[i])
    
    print(total)

if __name__ == "__main__":
    main()