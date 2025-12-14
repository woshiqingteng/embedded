""" 
@brief 图遍历
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    x, y = map(int, data[0].split())
    grid = [list(map(int, line.split())) for line in data[1:1+x]]
    
    stamps = []
    covered = [[False] * y for _ in range(x)]
    
    # check 2x2
    for i in range(x-1):
        for j in range(y-1):
            if grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1] == 1:
                stamps.append((i, j))
                for di, dj in [(0,0),(0,1),(1,0),(1,1)]:
                    covered[i+di][j+dj] = True
    
    # check 1
    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1 and not covered[i][j]:
                print("No")
                return
    
    # check adjacent
    for i, (i1, j1) in enumerate(stamps):
        for i2, j2 in stamps[i+1:]:
            if abs(i1-i2) <= 2 and abs(j1-j2) <= 2:
                print("No")
                return
    
    print("Yes")

if __name__ == "__main__":
    main()