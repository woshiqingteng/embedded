""" 
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))

    odd = []
    for x in arr:
        if x % 2 == 1:
            odd.append(x)
        else:
            odd.append(x - 1)
    
    total = sum(odd)
    if total % 2 == 1:
        print(total)
    else:
        print(total - min(odd))

if __name__ == "__main__":
    main()