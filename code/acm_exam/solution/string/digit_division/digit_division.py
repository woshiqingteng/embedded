"""
@brief 贪心
"""

def main():
    n = int(input().strip())
    s = str(n)
    
    count = 0
    for char in s:
        d = int(char)
        if d != 0 and n % d == 0:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()