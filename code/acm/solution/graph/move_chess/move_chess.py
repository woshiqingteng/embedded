""" 
@brief 状态机
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    positions = list(map(int, data[1].split()))
    m = int(data[2])
    operations = list(map(int, data[3:3 + m]))
    
    # initial
    SIZE = 2019
    occupied = [0] * (SIZE + 1)
    for pos in positions:
       occupied[pos] = 1
    
    # traverse
    for op in operations:
        current = op
        next = op + 1
        if 1 < next <= SIZE and occupied[current] == 1 and occupied[next] == 0:
            occupied[current] = 0
            occupied[next] = 1
    
    # output
    result = [str(i) for i in range(1, SIZE + 1) if occupied[i] == 1]
    print(" ".join(result))

if __name__ == "__main__":
    main()