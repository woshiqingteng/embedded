"""
@brief DFS

思路：
    DFS 超出边界或当前位置为 0 返回 0，最大块初始化为当前位置，将当前位置设为 0，上下左右遍历，返回最大块
    遍历矩阵，当前位置不为 0，块数 +1，块大小为当前位置 DFS，最大块更新为块大小和最大块的最大值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(map(int, data[i].split())) for i in range(1, n+1)]
    
    count = 0
    max_size = 0

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return 0
        
        total = grid[i][j]
        grid[i][j] = 0

        total += dfs(i + 1, j)
        total += dfs(i - 1, j)
        total += dfs(i, j + 1)
        total += dfs(i, j - 1)

        return total

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                count += 1
                size = dfs(i, j)
                max_size = max(size, max_size)
    
    print(count, max_size)

if __name__ == "__main__":
    main()