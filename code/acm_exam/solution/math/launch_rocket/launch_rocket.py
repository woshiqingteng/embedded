import sys
import math

def main():
    # input
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    array = [list(map(float, data[i].split())) for i in range(1, t+1)]

    for i in range(t):
        x, y, z, vx, vy, vz, R = array[i]
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