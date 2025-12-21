"""
@brief 数组去重

思路：
    构造字典，字典元素-1和与 k 比较
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    a = list(map(int, data[1].split()))

    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    count = sum(freq[x]-1 for x in freq)
    # count = n - len(set(a))
    result = "Yes" if count <= k else "No"
    
    print(result)

if __name__ == "__main__":
    main()