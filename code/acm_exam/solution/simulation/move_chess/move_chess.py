""" 
@brief 模拟

思路：
    使用一个数组记录棋子位置，初始化棋子位置，遍历操作，更新棋子位置
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    positions = list(map(int, data[1].split()))
    m = int(data[2])
    operations = list(map(int, data[3:3 + m]))
    
    SIZE = 2019
    occupied = [0] * (SIZE + 1)
    for pos in positions:
       occupied[pos] = 1
    
    for op in operations:
        curr = op
        nxt = op + 1
        if 1 < nxt <= SIZE and occupied[curr] == 1 and occupied[nxt] == 0:
            occupied[curr] = 0
            occupied[nxt] = 1
    
    result = [i for i in range(1, SIZE + 1) if occupied[i] == 1]
    print(*result)

if __name__ == "__main__":
    main()