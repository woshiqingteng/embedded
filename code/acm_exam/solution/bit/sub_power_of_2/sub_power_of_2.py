"""
@brief 位运算

思路：
    数组元素异或，统计二进制 1 的个数
"""

def min_op(a):
    bit_or = 0
    for num in a:
        bit_or |= num

    # count = bin(bit_or).count('1')
    count = 0
    while bit_or:
        count += bit_or & 1
        bit_or >>= 1

    return count

def main():
    a = list(map(int, input().split()))
    
    result = min_op(a)
    print(result)

if __name__ == "__main__":
    main()