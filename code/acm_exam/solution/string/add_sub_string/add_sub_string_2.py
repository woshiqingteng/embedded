""" 
@brief 队列

思路：
    从0-9遍历字符串，对每个遍历结果使用长度为k队列更新，并更新最小操作数
"""

import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    n, k = list(map(int, data[0].split()))
    a = data[1].strip()
    
    min_op = float("inf")
    for i in range(10):
        count = [abs(int(c) - i) for c in a]
        queue = deque()
        current = 0
        for j in range(n):
            queue.append(count[j])
            current += count[j]
            if len(queue) > k:
                current -= queue.popleft()
            if len(queue) == k:
                min_op = min(min_op, current)

    print(min_op)

if __name__ == "__main__":
    main()