"""
@brief 数论

思路：
    数组最大值减去数组最小值
"""

def main():
    a = list(map(int, input().split()))

    result = max(a) - min(a)
    
    print(result)

if __name__ == "__main__":
    main()