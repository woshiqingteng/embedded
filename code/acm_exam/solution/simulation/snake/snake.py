""" 
@brief 模拟
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(map(str, data[i].strip())) for i in range(1, n+1)]
    operations = str(data[n+1].strip())

    score = 0
    directions = {
        'W': (-1, 0),  # 上
        'S': (1, 0),   # 下
        'A': (0, -1),  # 左
        'D': (0, 1)    # 右
    }
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                x, y = i, j
                break
        if x != -1:
            break

    for op in operations:
        dx, dy = directions.get(op)
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
            if grid[x][y] == '$':
                score += 1
                grid[x][y] = '.'

    print(score)

if __name__ == "__main__":
    main()