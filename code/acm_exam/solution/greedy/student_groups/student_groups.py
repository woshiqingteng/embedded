"""
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    scores = list(map(int, data[1].split()))
    
    # sort
    scores.sort()
    
    count = 0
    i = 0
    while i < n:
        if i + 2 < n and scores[i + 2] - scores[i] <= 9:
            count += 1
            i += 3
        elif i + 1 < n and scores[i + 1] - scores[i] <= 19:
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()
