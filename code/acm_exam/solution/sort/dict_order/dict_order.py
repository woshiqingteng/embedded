"""
@brief 冒泡排序
"""

import sys

def main():
    data = sys.stdin.read().splitlines()    
    n = int(data[0])
    a = list(map(int, data[1].split()))

    count = [2] * (n + 1)
    for i in range(n):
        k = i
        for j in range(i + 1, min(i + 3, n)):
            if a[j] > a[k]:
                k = j
        
        while k > i and count[a[k]] > 0 and count[a[k-1]] > 0:
            a[k], a[k - 1] = a[k - 1], a[k]
            count[a[k]] -= 1
            count[a[k-1]] -= 1
            k -= 1

    print(*a)

if __name__ == "__main__":
    main()