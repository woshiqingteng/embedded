""" 
@brief 模拟

思路：
    单指针遍历字符串，并更新
"""

def main():
    s = input().strip()
    
    n = len(s)
    result = []
    d, i = 1, 0
    while i + d <= n:
        result.append(int(s[i:i + d], 2))
        i += d
        d = (d % 9) + 1

    print(*result)

if __name__ == "__main__":
    main()