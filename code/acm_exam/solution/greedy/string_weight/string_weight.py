"""
@brief 贪心

思路：
    遍历字符串，计算每个可能得权值，并更新最大值
"""

def cal_weight(s):
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord("a")] += 1
    even = sum(1 for count in freq if count > 0 and count % 2 == 0)
    odd = sum(1 for count in freq if count > 0 and count % 2 == 1)

    return even - odd

def main():
    s = input().strip()
    
    n = len(s)
    max_weight = float('-inf')
    for i in range(n + 1):
        total = cal_weight(s[:i]) + cal_weight(s[i:])
        max_weight = max(max_weight, total)
    
    print(max_weight)

if __name__ == "__main__":
    main()