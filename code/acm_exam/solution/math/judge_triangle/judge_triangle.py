""" 
@brief 几何

思路：
    三角形判定：a + b > c
    三角形相似：a[0] / b[0] = a[1] / b[1] = a[2] / b[2]
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
    data = sys.stdin.read().splitlines()
    a = list(map(int, data[0].split()))
    n = int(data[1])
    b = [list(map(int, data[i].split())) for i in range(2, n+2)]
    
    for sides in b:
        if not is_triangle(sides):
            print("Can not form a triangle")
        elif is_similar(a, sides):
            print("Similar")
        else:
            print("Can form a triangle but not similar")

if __name__ == "__main__":
    main()