""" 
@brief 贪心
"""

def main():
    # input
    s = input().strip()
    n = len(s)

    positions = [i for i, ch in enumerate(s) if ch == '1']
    k = len(positions)
    left = sum(positions[i] - i for i in range(k))
    right = sum((n - k + i) - positions[i] for i in range(k))

    print(max(left, right))

if __name__ == "__main__":
    main()