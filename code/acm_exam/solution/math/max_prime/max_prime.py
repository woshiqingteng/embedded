"""
@brief 数学

偶数全部2相加，奇数减1变成偶数，最后一个2，变为3
"""
def main():
    # read
    n = int(input())
    
    # solve
    if n % 2 == 0:
        print(n // 2)
    else:
        print((n - 1) // 2)

if __name__ == "__main__":
    main()