"""
@brief 手动构造

思路：
    辗转相除取余求最大公约数
    对最大公约数求最小质因数
"""

def my_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def min_prime(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n

def main():
    a, b, c, d = map(int, input().split())

    gcd = my_gcd(my_gcd(a, b), my_gcd(c, d))
    if gcd == 1:
        print(-1)
    else:
        print(min_prime(gcd))

if __name__ == "__main__":
    main()