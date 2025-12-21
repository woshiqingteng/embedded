""" 
@brief 贪心

思路：
    遍历输入字符串，列表索引每次增加索引+1
"""

def main():
    s = input().strip()

    count = [0] * 26
    for i, c in enumerate(s):
        count[ord(c) - ord("a")] += i + 1
        print(*count)

if __name__ == "__main__":
    main()