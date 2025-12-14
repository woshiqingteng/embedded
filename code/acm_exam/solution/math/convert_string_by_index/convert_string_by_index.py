""" 
@brief 数学
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    
    result = []
    for i, char in enumerate(s):
        count = bin(i).count('1')
        if count % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char)
    
    print(''.join(result))

if __name__ == "__main__":
    main()