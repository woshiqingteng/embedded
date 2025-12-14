"""
@brief 数学
"""

import sys

def my_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    a = [x for x in arr if x > 0]
    if a:
        g = a[0]
        for i in range(1, len(a)):
            g = my_gcd(g, a[i])
    else:
        g = 0

    result = len(a) * g
    print(result)

if __name__ == "__main__":
    main()