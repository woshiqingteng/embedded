"""
@brief 双指针
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = list(data[1].strip())

    for i in range(n - k + 1):
        # s[i:i+k] = s[i:i+k][::-1]
        left, right = i, i + k - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    print(''.join(s))

if __name__ == "__main__":
    main()