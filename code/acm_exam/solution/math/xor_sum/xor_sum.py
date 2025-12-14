""" 
@brief 数学
"""

import sys

def main():
    # input
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    
    xor = 0
    for num in arr:
        # count = bin(num).count('1')
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