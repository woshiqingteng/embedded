""" 
@brief 贪心

思路：
    循环添加数组小于均值元素到新数组，并将新数组赋给旧数组，循环
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    a = list(map(int, data[1].split()))
    
    count = 0
    while sum(a)/len(a) > min(a):
        avg = sum(a)/len(a)
        new_a = []
        for x in a:
            if avg <= x:
                new_a.append(x)
        count += 1
        a = new_a

    print(count)

if __name__ == "__main__":
    main()