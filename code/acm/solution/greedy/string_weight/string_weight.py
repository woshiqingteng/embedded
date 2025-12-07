"""
@brief 贪心
"""

import sys

def calculate(s):
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord('a')] += 1
    even = sum(1 for count in freq if count > 0 and count % 2 == 0)
    odd = sum(1 for count in freq if count > 0 and count % 2 == 1)

    return even - odd

def main():
    data = sys.stdin.readline().splitlines()
    s = str(data[0].strip())
    n = len(s)

    max_weight = float('-inf')
    
    for i in range(n + 1):
        total = calculate(s[:i]) + calculate(s[i:])
        max_weight = max(max_weight, total)
    
    print(max_weight)

if __name__ == "__main__":
    main()