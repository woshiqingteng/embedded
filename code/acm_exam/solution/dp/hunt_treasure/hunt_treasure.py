"""
@brief DP

思路：
    构建 DP 数组，并初始化
    从 1-n 遍历并更新 DP 数组，取 DP 最大值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = [tuple(map(int, data[i].split())) for i in range(1, n + 1)]
    
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][2]
    for i in range(1, n):
        a, b, c, d = arr[i]
        prev_b, prev_d = arr[i-1][1], arr[i-1][3]
        dp[i][0] = max(dp[i-1][0] + a, dp[i-1][1] + a - prev_d)
        dp[i][1] = max(dp[i-1][0] + c - prev_b, dp[i-1][1] + c)

    print(max(dp[n-1][0], dp[n-1][1]))

if __name__ == "__main__":
    main()