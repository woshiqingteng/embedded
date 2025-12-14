"""
@brief 贪心
"""

import sys
from collections import Counter

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, k = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    freq = Counter(a)
    used = set()
    count = 0
    for num in list(freq.keys()):
        if num in used:
            continue            
        comp = k - num
        if num == comp:
            count += freq[num] - 1
        elif comp in freq:
            count += min(freq[num], freq[comp])
            used.add(comp)
        used.add(num)
    
    # output
    print(count)

if __name__ == "__main__":
    main()