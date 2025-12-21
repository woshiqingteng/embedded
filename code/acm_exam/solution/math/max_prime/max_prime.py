"""
@brief 数学

思路：
    n 为偶数：全部2相加
    n 为奇数：先使用一个3，剩余用2填满，(n-3) // 2 + 1 = (n -1) // 2
    n // 2
"""

def main():
    n = int(input())

    print(n // 2)

if __name__ == "__main__":
    main()