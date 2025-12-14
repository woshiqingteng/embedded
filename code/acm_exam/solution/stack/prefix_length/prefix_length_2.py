""" 
@brief 计数
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = [data[i].strip() for i in range(1, n+1)]
    
    # solve
    def valid_prefix(s):
        balance = 0
        max_len = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                break
            if balance == 0:
                max_len = i + 1
        
        return max_len

    # output
    for string in s:
        print(valid_prefix(string))

if __name__ == "__main__":
    main()