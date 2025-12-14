""" 
@brief 数学
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    n = [int(data[i].split()[0]) for i in range(1, t+1)]
    k = [int(data[i].split()[1]) for i in range(1, t+1)]

    for i in range(t):
        # fast xor
        def fast_xor(n):
            mod = n & 3 # mod = n % 4
            if mod == 0:
                return n
            elif mod == 1:
                return 1
            elif mod == 2:
                return n + 1
            else:
                return 0
        # total_xor = 0
        # for j in range(1, n[i] + 1):
        #     total_xor ^= j
        missing = fast_xor(n[i]) ^ k[i]
      
        print(missing)

if __name__ == "__main__":
    main()