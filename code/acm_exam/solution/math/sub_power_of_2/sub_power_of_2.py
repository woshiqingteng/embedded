"""
@brief 位运算
"""

def min_op(a):
    bit_or = 0
    for num in a:
        bit_or |= num

    count = 0
    # count = bin(bit_or).count('1')
    while bit_or:
        count += bit_or & 1
        bit_or >>= 1

    return count

def main():
    # input
    a = list(map(int, input().split()))
    
    result = min_op(a)
    print(result)

if __name__ == "__main__":
    main()