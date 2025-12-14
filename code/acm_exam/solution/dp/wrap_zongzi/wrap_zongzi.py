"""
@brief DP
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m, c0, d0 = map(int, data[0].split())
    array = [list(map(int, data[i].split())) for i in range(1, m+1)]

    plan = []
    dp = [0] * (n + 1)

    # binary
    for i in range(m):
        a, b, c, d = array[i]
        max_count = min(a // b, n // c)
        k = 1
        while max_count > 0:
            count = min(k, max_count)
            plan.append((count * c, count * d))
            max_count -= count
            k <<= 1
    # unbounded
    for i in range(c0, n + 1):
        dp[i] = max(dp[i], dp[i - c0] + d0)
    # 0-1
    for cost, value in plan:
        for j in range(n, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + value)

    print(dp[n])

if __name__ == "__main__":
    main()