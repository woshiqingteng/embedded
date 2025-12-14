""" 
@brief 贪心
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    a = str(data[0].strip())
    b = str(data[1].strip())
    
    total = 0
    for i in range(4):
        total += (int(a[i]) - int(b[i])) % 10
    
    print(total)

if __name__ == "__main__":
    main()