"""
@brief 统计

思路：
    中位数、均值、极值
"""

import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    arr = list(map(int, data[1].split()))
    a, b, c = map(int, data[2].split())

    score = sorted(arr)
    mid = n // 2
    median = score[mid] if n % 2 else (score[mid-1] + score[mid]) // 2
    mean = sum(score) // n
    trimmed = sum(score[1:-1]) // (n-2) if n > 2 else 0
    if  median >= a or mean >= b or trimmed >= c:
        result = "Yes"
    else:
        result = "No"
    
    print(result)

if __name__ == "__main__":
    main()