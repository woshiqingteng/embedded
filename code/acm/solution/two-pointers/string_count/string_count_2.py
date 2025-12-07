""" 
@brief 枚举
"""

def main():
    # input
    s = input().strip()
    n = len(s)
    
    # solve
    count = 0
    for i in range(n):
        for j in range(i, n):
            if 'd' in s[i:j+1]:
                continue
            if 'r' in s[i:j+1] and 'e' in s[i:j+1]:
                count += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()