""" 
@brief 贪心

思路：
    计算问询价值并排序，按照价值构造数组
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m, k = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    gain = [(x * x - x, i) for i, x in enumerate(a)]
    gain.sort(key=lambda x: x[0], reverse=True)
    for i in range(k):
        idx = gain[i][1]
        a[idx] = a[idx] * a[idx]
    a.sort(reverse=True)

    result = []
    count = 0
    for i in range(m):
        count += a[i]
        result.append(count)
    
    print(*result)

if __name__ == "__main__":
    main()