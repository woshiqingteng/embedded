"""
@brief 集合去重

思路：
    所有字母和减去出现字母和
"""

def main():
    s = input().strip()
    
    total = sum(range(65, 91))
    appeared = sum(ord(c) for c in set(s))

    result = total - appeared
    print(result)

if __name__ == "__main__":
    main()