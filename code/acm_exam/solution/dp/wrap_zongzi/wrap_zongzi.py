"""
@brief DP

思路：
    二进制拆分将多重背包转化为0-1背包
    有馅粽子：0-1背包，逆序遍历，每个物品只使用1次
    无馅粽子：完全背包，正序遍历，允许无限次使用
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m, c0, d0 = map(int, data[0].split())
    arr = [list(map(int, data[i].split())) for i in range(1, m+1)]

    plan = []
    dp = [0] * (n + 1)
    # binary
    for i in range(m):
        a, b, c, d = arr[i]
        count = min(a // b, n // c)
        k = 1
        while count > 0:
            take = min(k, count)
            plan.append((take * c, take * d))
            count -= take
            k <<= 1
    # 0-1
    for cost, value in plan:
        for i in range(n, cost - 1, -1):
            dp[i] = max(dp[i], dp[i - cost] + value)
    # unbounded
    for i in range(c0, n + 1):
        dp[i] = max(dp[i], dp[i - c0] + d0)
    
    print(dp[n])

if __name__ == "__main__":
    main()