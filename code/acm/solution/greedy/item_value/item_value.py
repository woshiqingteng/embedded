""" 
@brief 贪心
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n, m, k = map(int, data[0].split())
    a = list(map(int, data[1].split()))
    
    gain = [(a[i] * a[i] - a[i], i) for i in range(n)]
    gain.sort(key=lambda x: x[0], reverse=True)
    
    for i in range(k):
        idx = gain[i][1]
        a[idx] = a[idx] * a[idx]
    
    a.sort(reverse=True)

    result = []
    current = 0
    for i in range(m):
        current += a[i]
        result.append(str(current))
    
    print(" ".join(result))

if __name__ == "__main__":
    main()