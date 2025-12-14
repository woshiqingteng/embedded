"""
@brief BFS
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(str(data[i].strip())) for i in range(1, n+1)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 'B':
                        count += 1
                        break

    print(count)

if __name__ == "__main__":
    main()