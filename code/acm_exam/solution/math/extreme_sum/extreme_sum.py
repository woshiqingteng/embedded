""" 
@brief 数论

思路：
    最优解中每个子序列要么是单元素，要么包含一个最大值和一个最小值
    最优配对是最大的 t 个数与最小的 t 个数配对
    最优 t = min(k, n-k)
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    a.sort()
    t = min(k, n-k)
    result = sum(a[-t:]) - sum(a[:t])
    
    print(result)

if __name__ == "__main__":
    main()