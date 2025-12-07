"""
@brief DFS
"""

import sys

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

    # traverse
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                count += 1
                size = dfs(i, j)
                max_size = max(size, max_size)
    
    print(count, max_size)

if __name__  == "__main__":
    main()