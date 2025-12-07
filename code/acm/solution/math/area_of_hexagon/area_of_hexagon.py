""" 
@brief 数学
"""

import sys
import math

def main():
    # input
    data = sys.stdin.read().splitlines()
    scores = list(map(float, data[0].split()))
    L = float(data[1])
        
    # solve
    area = 0.0
    for i in range(6):
        j = (i + 1) % 6
        area += 0.5 * (scores[i]*L/100) * (scores[j]*L/100) * math.sin(math.pi / 3)
    
    # output
    print(f"{area:.6f}")

if __name__ == "__main__":
    main()