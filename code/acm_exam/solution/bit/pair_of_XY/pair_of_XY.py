"""
@brief 位运算

思路：
    X + Y = X OR Y + X AND Y = A + B
    A <= X <= Y <= B
"""

def main():
    a, b = map(int, input().split())

    count = 0
    i, j = a, b
    while i <= j:
        if i & j == a and i | j == b:
            count +=1
        i += 1
        j -= 1
    
    print(count)

if __name__ == '__main__':
    main()