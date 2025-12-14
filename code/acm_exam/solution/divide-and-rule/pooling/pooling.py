""" 
@brief 分治
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    matrix = [list(map(int, data[i].split())) for i in range(1, n+1)]
    
    # solve
    def solve(matrix):
        n = len(matrix)
        while n > 1:
            new_size = n // 2
            new_matrix = [[0] * new_size for _ in range(new_size)]
            
            for i in range(0, n, 2):
                for j in range(0, n, 2):
                    nums = [
                        matrix[i][j], matrix[i][j+1],
                        matrix[i+1][j], matrix[i+1][j+1]
                    ]
                    new_matrix[i//2][j//2] = sorted(nums)[-2]
            matrix = new_matrix
            n = new_size
        
        return matrix[0][0]
    
    result = solve(matrix)

    # output
    print(result)

if __name__ == "__main__":
    main()