""" 
@brief 双指针
"""

def main():
    # input
    s = input().strip()
    n = len(s)
    
    # solve
    count = 0
    for i in range(n):
        has_r = False
        has_e = False
        has_d = False
        for j in range(i, n):
            char = s[j]
            # check str
            if char == 'r':
                has_r = True
            elif char == 'e':
                has_e = True
            elif char == 'd':
                has_d = True
                break
            if has_r and has_e and not has_d:
                count += 1
    
    # output
    print(count)

if __name__ == "__main__":
    main()