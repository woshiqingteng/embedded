""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    k = list(map(int, data[1:n+1]))

    def solve(k):
        max_volume = 1
        i = 2
        while True:
            current = 1 + i * i
            if current <= k:
                max_volume = current
                i += 1
            else:
                break
        return max_volume
    
    # output
    for i in range(n):
        print(solve(k[i]))

if __name__ == '__main__':
    main()