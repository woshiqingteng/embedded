"""
@brief 贪心

思路：
    区间重叠条件：两区间左边界小于右边界
    顺序读取区间，重叠标志位设为 0，若重叠，重叠标志位设为 1，中断，不重叠，选择数组增加该区间，计数 +1
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    a = [tuple(map(int, data[i].split())) for i in range(1, t+1)]
    
    selected = []
    count = 0
    for i in range(t):
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