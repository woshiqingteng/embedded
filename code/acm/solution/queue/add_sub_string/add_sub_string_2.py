""" 
@brief 队列
"""

import sys
from collections import deque

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, k = list(map(int, data[0].split()))
    s = data[1].strip()
    
    # solve
    min_operations = float('inf')
    for target in range(10):
        costs = [abs(int(char) - target) for char in s]
        window = deque()
        current_sum = 0
        for i in range(n):
            window.append(costs[i])
            current_sum += costs[i]
            if len(window) > k:
                current_sum -= window.popleft()
            if len(window) == k:
                min_operations = min(min_operations, current_sum)
    
    # output
    print(min_operations)

if __name__ == "__main__":
    main()