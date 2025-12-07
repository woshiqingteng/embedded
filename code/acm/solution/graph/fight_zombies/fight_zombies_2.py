"""
@brief BFS
"""

import sys
from collections import deque

def main():
    # read
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, n+1):
        row = list(map(int, data[i].split()))
        grid.append(row)
    
    # initial
    count = 0
    max_size = 0

    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
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

    # traverse
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                count += 1
                size = bfs(i, j)
                max_size = max(size, max_size)
    
    print(count, max_size)

if __name__  == "__main__":
    main()