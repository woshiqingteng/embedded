""" 
@brief 数学
"""

import sys

def is_triangle(sides):
    a, b, c = sorted(sides)

    return a + b > c

def is_similar(base, sides):
    a = sorted(base)
    b = sorted(sides)

    return (a[0] * b[1] == a[1] * b[0] and a[0] * b[2] == a[2] * b[0] and a[1] * b[2] == a[2] * b[1])

def main():
    # input
    data = sys.stdin.read().splitlines()
    base = list(map(int, data[0].split()))
    n = int(data[1])
    test = [list(map(int, data[i].split())) for i in range(2, n+2)]
    
    # solve
    for sides in test:
        if not is_triangle(sides):
            print("Can not form a triangle")
        elif is_similar(base, sides):
            print("Similar")
        else:
            print("Can form a triangle but not similar")

if __name__ == "__main__":
    main()