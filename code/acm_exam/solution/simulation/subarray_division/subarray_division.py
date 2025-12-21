"""
@brief 模拟

思路：
    计算前缀和，k 数组从 k-1 到 n 开始遍历，k-1 数组从 k-2 到 i 开始遍历
    k = 2 特殊情况，非零跳过
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    arr = list(map(int, data[1].split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    for i in range(k - 1, n):
        a = prefix[n] - prefix[i]
        for j in range(k - 2, i):
            if k == 2 and j != 0: 
                continue
            b = prefix[i] - prefix[j]
            if b != 0 and a % b == 0:
                print("Yes")
                return
    
    print("No")

if __name__ == "__main__":
    main()