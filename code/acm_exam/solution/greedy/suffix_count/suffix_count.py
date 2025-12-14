""" 
@brief 贪心
"""

def main():
    s = input().strip()

    counts = [0] * 26
    for i, ch in enumerate(s):
        counts[ord(ch) - ord('a')] += i + 1
        print(' '.join(map(str, counts)))

if __name__ == "__main__":
    main()