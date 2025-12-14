"""
@brief list
"""

def main():
    # input
    s = str(input().strip())
    
    appeared = [False] * 26
    for ch in s:
        appeared[ord(ch) - ord('A')] = True
    result = sum(ord('A') + i for i in range(26) if not appeared[i])

    print(result)

if __name__ == "__main__":
    main()