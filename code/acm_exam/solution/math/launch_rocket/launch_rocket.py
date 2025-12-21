""" 
@brief 几何

思路：
    解一元二次方程：(x+vx*t)^2 + (y+vy*t)^2 + (z+vz*t)^2 = R^2
"""

import sys
import math

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    at = [list(map(float, data[i].split())) for i in range(1, t+1)]

    for i in range(t):
        x, y, z, vx, vy, vz, R = at[i]
        a = vx*vx + vy*vy + vz*vz
        b = 2*(x*vx + y*vy + z*vz)
        c = x*x + y*y + z*z - R*R
        delta = b*b - 4*a*c

        if delta < 0:
            result = 0
        else:
            t1 = (-b + math.sqrt(delta)) / (2*a)
            t2 = (-b - math.sqrt(delta)) / (2*a)
            if t1 > 0 and t2 > 0:
                result = min(t1, t2)
            elif t1 > 0:
                result = t1
            elif t2 > 0:
                result = t2
            else:
                result = 0

        print(f"{result:.2f}")

if __name__ == "__main__":
    main()