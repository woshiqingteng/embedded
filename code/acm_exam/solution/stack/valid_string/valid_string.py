"""
@brief 栈
"""

def main():
    s = input().strip()

    count = 0
    for char in s:
        if char == 'a':
            count += 1
        elif char == 'b':
            count -= 1
            if count < 0:
                print("NO")
                return

    print("YES" if count == 0 else "NO")

if __name__ == "__main__":
    main()