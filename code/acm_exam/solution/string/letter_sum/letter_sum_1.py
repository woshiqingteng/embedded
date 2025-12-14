"""
@brief set
"""

def main():
    # input
    s = str(input().strip())
    
    total = sum(range(65, 91))
    appeared = sum(ord(ch) for ch in set(s))

    result = total - appeared
    print(result)

if __name__ == "__main__":
    main()