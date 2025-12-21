""" 
@brief 模拟

思路：
    初始化位置和操作，BFS 搜索
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    a = [list(data[i].strip()) for i in range(1, n+1)]
    b = list(data[n+1].strip())

    score = 0
    directions = {
        "W": (-1, 0),
        "S": (1, 0), 
        "A": (0, -1),
        "D": (0, 1)  
    }
    x, y = next(((i, j) for i in range(n) for j in range(m) if a[i][j] == '*'), (-1, -1))

    for op in b:
        dx, dy = directions.get(op)
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == "$":
            score += 1
            a[x][y] = "."

    print(score)

if __name__ == "__main__":
    main()