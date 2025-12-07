"""
@brief 数学
"""

import sys

def my_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    # read
    data = sys.stdin.read().split()
    a, b, c, d = map(int, data)
    
    # solve
    gcd = my_gcd(my_gcd(a, b), my_gcd(c, d))

    if gcd == 1:
        print(-1)
        return
    
    for i in range(2, int(gcd**0.5) + 1):
        if gcd % i == 0:
            print(i)
            return

    print(gcd)

if __name__ == "__main__":
    main()