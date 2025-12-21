""" 
@brief 位运算

思路：
    lowbit(x) = x & -x
"""

def main():
    n = int(input().strip())

    total = 0
    for i in range(1, n + 1):
        fx = i & -i
        total += i // fx
    
    print(total)

if __name__ == "__main__":
    main()