""" 
@brief 模拟

思路：
    单指针循环构造矩阵
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [list(map(int, data[i].split())) for i in range(1, n+1)]
    
    while n > 1:
        new_size = n // 2
        new_a = [[0] * new_size for _ in range(new_size)]
        for i in range(0, n, 2):
            for j in range(0, n, 2):
                aj = [
                    a[i][j], a[i][j+1],
                    a[i+1][j], a[i+1][j+1]
                ]
                new_a[i//2][j//2] = sorted(aj)[-2]
        a, n = new_a, new_size
    
    result =  a[0][0]

    print(result)

if __name__ == "__main__":
    main()