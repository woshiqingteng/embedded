"""
@brief 数学
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    scores = [list(map(int, data[i].split())) for i in range(1, m+1)]
    
    bless = [0] * n

    for j in range(m):
        avg = sum(scores[j])/n
        for i in range(n):
            if scores[j][i] > avg:
                bless[i] = 1

    print(sum(bless))

if __name__ == "__main__":
    main()