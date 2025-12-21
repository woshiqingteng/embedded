""" 
@brief 手动构造

思路：
    统计数组中元素二进制 1 的个数并求和
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    xor = 0
    for num in a:
        count = 0
        temp = num
        while temp:
            count += temp & 1
            temp >>= 1
        if count % 2 == 0: 
            xor ^= num 

    print(xor)

if __name__ == "__main__":
    main()