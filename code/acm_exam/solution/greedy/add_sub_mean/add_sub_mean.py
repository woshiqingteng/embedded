""" 
@brief 贪心

思路：
    数组小于 k 元素提升到 k，记录操作数
    提升后总和与 n x m 的差值的绝对值
    两个相加
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m, k = list(map(int, data[0].split()))
    a = list(map(int, data[1].split()))

    count = 0
    total = 0
    for x in a:
        count += max(k - x, 0)
        total += max(x, k)

    reuslt = count + abs(total - n * m)
    
    print(reuslt)

if __name__ == "__main__":
    main()