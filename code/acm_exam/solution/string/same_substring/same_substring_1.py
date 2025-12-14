"""
@brief list
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    a = data[1].strip()
            
    count = [0] * 26
    i = 0
    while i <= n - k:
        if a[i:i+k] == a[i] * k:
            count[ord(a[i]) - ord('a')] += 1
            i += k
        else:
            i += 1

    print(max(count))

if __name__ == "__main__":
    main()