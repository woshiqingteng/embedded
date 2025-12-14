"""
@brief 贪心
"""

import sys
from collections import defaultdict

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))

    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    count = sum(freq[num]-1 for num in freq)
    # count = n - len(set(arr))
    result = "Yes" if count <= k else "No"
    
    print(result)

if __name__ == "__main__":
    main()