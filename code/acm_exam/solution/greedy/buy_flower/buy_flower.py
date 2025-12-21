""" 
@brief 贪心

思路：
    构造奇数数组：奇数添加，偶数-1添加
    数组求和，和为奇数，结果为和，和为偶数，结果为和减去奇数数组最小值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))

    odd = [x if x % 2 else x - 1 for x in a]    
    total = sum(odd)
    result = total if total % 2 else total - min(odd)

    print(result)

if __name__ == "__main__":
    main()