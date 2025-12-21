""" 
@brief 暴力枚举

思路：
    遍历字符串，条件判断并更新计数器
"""

def main():
    s = input().strip()

    n = len(s)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n+1):
            if "d" in s[i:j]:
                continue
            if "r" in s[i:j] and "e" in s[i:j]:
                count += 1

    print(count)

if __name__ == "__main__":
    main()