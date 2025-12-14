"""
@brief enumerate
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()