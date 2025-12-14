""" 
@brief 枚举
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, k = list(map(int, data[0].split()))
    s = data[1].strip()
    
    # solve
    min_operations = float('inf')
    for i in range(n - k + 1):
        substring = s[i:i+k]
        for target in range(10):
            operations = 0
            for char in substring:
                operations += abs(int(char) - target)
            min_operations = min(min_operations, operations)
    
    # output
    print(min_operations)

if __name__ == "__main__":
    main()