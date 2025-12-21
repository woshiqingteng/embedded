"""
@brief 模拟

思路：
    遍历字符串，并反转固定长度子串
    字符串转换为列表使用切片
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    s = data[1].strip()

    sl = list(s)
    for i in range(n - k + 1):
        # s[i:i+k] = s[i:i+k][::-1]
        left, right = i, i + k - 1
        while left < right:
            sl[left], sl[right] = sl[right], sl[left]
            left += 1
            right -= 1
    
    print("".join(sl))

if __name__ == "__main__":
    main()