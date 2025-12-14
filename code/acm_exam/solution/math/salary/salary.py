"""
@brief 数学
"""

def main():
    a, b, n = map(int, input().split())
    
    total = 0
    for i in range(1, n + 1):
        total += a + (i - 1) * b
    #  total = n * a +  n * (n - 1) * b // 2
    
    print(total)

if __name__ == "__main__":
    main()