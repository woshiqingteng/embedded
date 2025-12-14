"""
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    T = int(data[0])
    a = [list(map(int, data[i].split())) for i in range(1, T+1)]
    
    selected = []
    count = 0
    for i in range(T):
        l, r = a[i]
        overlap = False
        for start, end in selected:
            if max(l, start) <= min(r, end):
                overlap = True
                break
        if not overlap:
            selected.append((l, r))
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()