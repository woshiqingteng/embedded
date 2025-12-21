"""
@brief DP

思路：
    合并相同时间、位置地鼠，并按照时间排序
    从头遍历 DP 更新初始位置，从当前反向遍历，更新 DP
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m, k = map(int, data[0].split())
    a = [list(map(int, data[i].split())) for i in range(1, k+1)]

    b = {}
    for x, y, t, s in a:
        key = (x, y, t)
        b[key] = b.get(key, 0) + s
    c = [[x, y, t, s] for (x, y, t), s in b.items()]
    c.sort(key=lambda x: x[2])
    dp = [0] * len(c)

    for i in range(len(c)):
        xi, yi, ti, si = c[i]
        dp[i] = si if abs(xi - 1) + abs(yi - 1) <= ti else 0
        for j in range(i - 1, -1, -1):
            xj, yj, tj, sj = c[j]
            if abs(xi - xj) + abs(yi - yj) <= ti - tj and dp[j] > 0:
                dp[i] = max(dp[i], dp[j]+si)

    print(max(dp))

if __name__ == "__main__":
    main()