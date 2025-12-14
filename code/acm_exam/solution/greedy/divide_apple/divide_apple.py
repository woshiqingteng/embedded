""" 
@brief 贪心
"""

def main():
    # input
    n, m, k = list(map(int, input().split()))

    def check(x):
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
        if check(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(result)

if __name__ == "__main__":
    main()