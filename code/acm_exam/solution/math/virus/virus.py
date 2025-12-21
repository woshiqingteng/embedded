""" 
@brief 数论

思路：
    平方和累加，不超过 k，更新最大值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = [int(data[i]) for i in range(1, n+1)]

    for k in a:
        max_v = 1
        t, v = 2, 1
        while True:
            v += t * t
            if k >= v:
                max_v = v
                t += 1
            else:
                break

        print(max_v)
    
if __name__ == "__main__":
    main() 