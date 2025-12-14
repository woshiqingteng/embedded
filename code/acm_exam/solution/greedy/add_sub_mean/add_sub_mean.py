""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, m, k = list(map(int, data[0].split()))
    array = list(map(int, data[1].split()))

    # solve
    count = 0
    total = 0
    for num in array:
        count += max(k - num, 0)
        total += max(num, k)

    count += abs(total - n * m)
    
    # output
    print(count)

if __name__ == "__main__":
    main()