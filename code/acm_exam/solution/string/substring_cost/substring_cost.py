"""
@brief 滑动窗口
"""

def cost(c1, c2):
    a = 0 if c1.lower() == c2.lower() else 5
    b = 0 if c1.isupper() == c2.isupper() else 5
    return a + b

def main():
    # input
    s = str(input().strip())
    if n < len(t):
        print(-1)
        return
    
    t = "AcMer"
    n = len(s)
    min_cost = float('inf')

    for i in range(n - len(t) + 1):
        current = 0
        for j in range(len(t)):
            current += cost(s[i + j], t[j])
        min_cost = min(min_cost, current)

    # output
    print(min_cost)

if __name__ == "__main__":
    main()