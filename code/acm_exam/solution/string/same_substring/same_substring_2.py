"""
@brief dict
"""

import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    a = data[1].strip()
            
    count = defaultdict(int)
    i = 0
    while i <= n - k:
        if a[i:i+k] == a[i] * k:
            count[a[i]] += 1
            i += k
        else:
            i += 1

    result = max(count.values()) if count else 0
    print(result)

if __name__ == "__main__":
    main()