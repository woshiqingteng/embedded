""" 
@brief 贪心

思路：
    分别计算所有 1 在左边和右边的次数，取最大值
"""

def main():
    s = input().strip()
    n = len(s)

    positions = [i for i, c in enumerate(s) if c == "1"]
    k = len(positions)
    left = sum(positions[i] - i for i in range(k))
    right = sum((n - k + i) - positions[i] for i in range(k))

    print(max(left, right))

if __name__ == "__main__":
    main()