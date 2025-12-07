""" 
@brief 模拟
"""

import sys

def main():
    # read
    data = sys.stdin.read().splitlines()
    s = data[0].strip()
    n = len(s)

    result = []
    step = 1
    index = 0

    while index + step <= n:
        sub = s[index:index + step]
        decimal = int(sub, 2)
        result.append(str(decimal))

        index += step
        step = (step % 9) + 1

    # output
    print(" ".join(result))

if __name__ == "__main__":
    main()