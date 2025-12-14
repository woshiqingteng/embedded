"""
@brief 位运算

X + Y = X OR Y + X AND Y = A + B
A <= X <= Y <= B
"""
import sys

def main():
    data = sys.stdin.read().splitlines()
    A, B = map(int, data[0].split())

    count = 0
    i, j = A, B
    while i <= j:
        if i & j == A and i | j == B:
            count +=1
        i += 1
        j -= 1
    
    print(count)

if __name__ == '__main__':
    main()