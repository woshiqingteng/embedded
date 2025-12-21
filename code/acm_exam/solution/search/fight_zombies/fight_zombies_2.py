"""
@brief BFS

思路：
    BFS 队列和最大块初始化初始化为当前位置，遍历队列，将当前位置设为 0，上下左右遍历，
    在范围内且位置不为 0，队列添加当前位置，最大块加当前位置，当前位置设为 0
    遍历矩阵，当前位置不为 0，块数 +1，块大小为当前位置 BFS，最大块更新为块大小和最大块的最大值
"""

import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(map(int, data[i].split())) for i in range(1, n+1)]
    
    count = 0
    max_size = 0

    def bfs(i, j):
        queue = deque([(i, j)])
        total = grid[i][j]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y = queue.popleft()
            grid[x][y] = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0:
                    queue.append((nx, ny))
                    total += grid[nx][ny]
                    grid[nx][ny] = 0

        return total

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                count += 1
                size = bfs(i, j)
                max_size = max(size, max_size)
    
    print(count, max_size)

if __name__  == "__main__":
    main()