"""
@brief eval

思路：
    遍历字符串，eval 并更新最大值
"""

def main():
    s = input().strip()
    
    n = len(s)
    max_result = float('-inf')
    
    for i in range(n):
        string = s[:i] + s[i+1:]
        try:
            result = eval(string)
            max_result = max(max_result, result)
        except:
            continue

    print(max_result)

if __name__ == "__main__":
    main()