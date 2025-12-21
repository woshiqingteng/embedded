"""
@brief 构造列表

思路：
    所有字母和减去出现字母和
"""

def main():
    s = input().strip()
    
    appeared = [False] * 26
    for c in s:
        appeared[ord(c) - ord("A")] = True
    result = sum(ord("A") + i for i in range(26) if not appeared[i])

    print(result)

if __name__ == "__main__":
    main()