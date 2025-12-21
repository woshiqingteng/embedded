"""
@brief 贪心

思路：
    计算周期数、剩余子弹数、每个周期最小时间、剩余子弹数计算最小时间
"""

def main():
    n, m, a, b = map(int, input().split())
    
    last = 0
    count, remain = n // m, n % m
    cycle = min(a+m, m*(b+1))
    if remain > 0:
        last = min(a+remain, remain*(b+1))
    
    total = count * cycle + last
    print(total)

if __name__ == "__main__":
    main()