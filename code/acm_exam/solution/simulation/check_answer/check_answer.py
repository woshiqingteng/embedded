""" 
@brief 模拟

思路：
    比较答案正确数量
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    a = data[0].strip()
    b = data[1].strip()

    n = len(a)
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1

    if count > n - count:
        print("Oh Yes")
    elif count < n - count:
        print("Oh No")
    else:
        print("(O.O)")

if __name__ == "__main__":
    main()