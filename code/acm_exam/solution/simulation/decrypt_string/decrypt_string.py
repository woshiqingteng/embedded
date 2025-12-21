"""
@brief 模拟

思路：
    遍历字符串，元音字母，添加到结果
    其他，根据条件，更新字符
"""

def main():
    s = input().strip()
    
    v = list("aeiou")
    result = []
    
    for c in s:
        if c in v:
            result.append(c)
        else:
            dist = [(abs(ord(c) - ord(x)), x) for x in v]
            target = min(dist)[1]
            result.append(c + target + c.upper())
    
    print("".join(result))

if __name__ == "__main__":
    main()