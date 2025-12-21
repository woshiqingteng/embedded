""" 
@brief 二分查找

思路：
    检查函数：小明 x 个苹果，左侧苹果数 max(1, x - i) 求和，右侧苹果数 max(1, x - j) 求和，总苹果数小于等于 m 返回真
    对苹果数进行二分查找
"""

def main():
    n, m, k = list(map(int, input().split()))

    def is_valid(x):
        total = x
        for i in range(1, k):
            total += max(1, x - i)
        for j in range(1, n - k + 1):
            total += max(1, x - j)
        return total <= m
    
    left, right = 1, m
    result = 1
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(result)

if __name__ == "__main__":
    main()