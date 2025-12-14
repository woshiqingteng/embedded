"""
@brief 双指针
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))

    count = 0
    left, right = 0, n - 1
    while left < right:
        diff = a[left] - a[right]
        if diff > 0:
            a[right] += diff
            a[right-1] += diff
            count += diff  
        elif diff < 0:
            a[left] += -diff
            a[left+1] += -diff
            count += -diff  
        left += 1
        right -= 1
    for i in range(n // 2):
        if a[i] != a[n - 1 - i]:
            count = -1
            break

    print(count)

if __name__ == "__main__":
    main()