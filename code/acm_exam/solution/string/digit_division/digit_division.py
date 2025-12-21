"""
@brief 数论

思路：
    遍历数字字符串，对每一位进行条件判定并计数
"""

def main():
    n = int(input().strip())
    
    s = str(n)
    count = 0
    for c in s:
        d = int(c)
        if d != 0 and n % d == 0:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()